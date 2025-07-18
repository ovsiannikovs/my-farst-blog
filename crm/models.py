from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


class Notifications(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    text = models.TextField(blank=True, null=True, verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
        ordering = ['-created_date']


class Customer(models.Model):
    name_of_company = models.CharField(max_length=255, verbose_name='Название компании', default='Без названия')
    revenue_for_last_year = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name='Выручка за последний год', help_text='Миллиард рублей')
    length_of_electrical_network_km = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Длина сетей, км')
    quantity_of_technical_transformer_pcs = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество ТП, шт')
    address = models.TextField(blank=True, null=True, verbose_name='Адрес')

    def __str__(self):
        return self.name_of_company

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        ordering = ['name_of_company']


class Decision_maker(models.Model):
    class TypeOfFunction(models.IntegerChoices):
        DIRECTOR = 0, 'директор'
        CHIEF_ENGINEER = 1, 'главный инженер'
        TECHNICAL_SPECIALIST = 2, 'технический специалист'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='лпр_листы', null=False,
    blank=False, verbose_name='Заказчик')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    city_of_location = models.CharField(max_length=100, blank=True, null=True,verbose_name='Город местонахождения')
    function = models.IntegerField(choices=TypeOfFunction.choices, default=TypeOfFunction.DIRECTOR, blank=True, null=True, verbose_name='Роль')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')
    email = models.EmailField(max_length=54, blank=True, null=True, verbose_name='Почта')
    telegram = models.CharField(max_length=50, blank=True, null=True, verbose_name='Телеграм')
    description_and_impression = models.TextField(blank=True, null=True, verbose_name='Описание и впечатления')

    def __str__(self):
        return f"{self.full_name} ({self.function})"

    class Meta:
        verbose_name = 'ЛПР'
        verbose_name_plural = 'ЛПР'
        ordering = ['full_name']


class Product(models.Model):
    name_of_product = models.CharField(max_length=255, verbose_name='Название')
    end_customer_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name='Цена для конечного заказчика')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name_of_product

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name_of_product']


class Deal(models.Model):
    SELECTION = [
        ('подготовлен_звонок', 'Подготовлен звонок'),
        ('сделан_звонок', 'Сделан звонок'),
        ('назначена_встреча', 'Назначена встреча'),
        ('прошла_встреча', 'Прошла встреча'),
        ('достигнута_договоренность', 'Достигнута договоренность'),
        ('готовится_договор', 'Готовится договор'),
        ('заключен_договор', 'Заключен договор'),
        ('исполнена_поставка', 'Исполнена поставка'),
        ('выполнен_монтаж', 'Выполнен монтаж'),
        ('идет_гарантийный_срок', 'Идет гарантийный срок'),
        ('послегарантийная_работа', 'Послегарантийная работа'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='сделки', blank=True, null=True, verbose_name='Заказчик')
    start_date = models.DateField(blank=True, null=True, verbose_name='Дата начала')
    date_of_last_change = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата последнего изменения')
    date_of_next_activity = models.DateField(blank=True, null=True, verbose_name='Дата следующей активности')
    status = models.CharField(max_length=50, choices=SELECTION, blank=True, null=True, verbose_name='Состояние')
    name_of_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Продукт')
    deal_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name='Сумма сделки')
    quantity_of_all_product = models.PositiveIntegerField(default=1, blank=True, null=True, verbose_name='Количество всех продуктов, шт')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    shipping_address = models.TextField(verbose_name='Адрес отгрузки', blank=True, null=True)
    responsible_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Ответственный менеджер')

    def __str__(self):
        return f"Сделка #{self.id} - {self.customer.name_of_company}"

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
        ordering = ['-start_date']


class Deal_stage(models.Model):
    SELECTION = Deal.SELECTION  # Используем те же варианты, что и для Сделки

    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name='этапы_сделки', blank=True, null=True, verbose_name='Сделка')
    start_date_step = models.DateField(blank=True, null=True, verbose_name='Дата начала этапа')
    end_date_step = models.DateField(blank=True, null=True, verbose_name='Дата конца этапа')
    status = models.CharField(max_length=50, choices=SELECTION, blank=True, null=True, verbose_name='Состояние')
    description_of_task_at_stage = models.TextField(blank=True, null=True, verbose_name='Описание задач на этап')
    description_of_what_has_been_achieved_at_a_stage = models.TextField(blank=True, null=True, verbose_name='Описание достигнутого на этапе')
    description_of_tasks_for_our_specialists = models.TextField(blank=True, null=True, verbose_name='Описание задач для наших специалистов')
    our_specialists_involved = models.ManyToManyField(User, related_name='этапы_сделки', blank=True, default=0, verbose_name='Привлекаемые наши специалисты')

    def __str__(self):
        return f"Этап {self.get_status_display()} для сделки #{self.deal.id}"

    class Meta:
        verbose_name = 'Этап сделки'
        verbose_name_plural = 'Этапы сделки'
        ordering = ['start_date_step']

class Call(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Заказчик')
    decision_maker = models.ForeignKey(Decision_maker, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ЛПР')
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Ответственный')
    planned_date = models.DateField(blank=True, null=True, verbose_name='Плановая дата')
    call_goal = models.CharField(max_length=200, blank=True, null=True, verbose_name='Описание цели звонка')
    call_result = models.CharField(max_length=200, blank=True, null=True, verbose_name='Описание результата')
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сделка (если есть)')

    def __str__(self):
        return f"Звонок по {self.customer.name_of_company} от {self.planned_date}"

    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'
        ordering = ['-planned_date']


class Letter(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Заказчик')
    decision_maker = models.ForeignKey(Decision_maker, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ЛПР')
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Ответственный')
    planned_date = models.DateField(blank=True, null=True, verbose_name='Плановая дата')
    letter_file = models.FileField(upload_to='letters/', blank=True, null=True, verbose_name='Тело письма')
    incoming_number = models.CharField(max_length=50, blank=True, null=True, verbose_name='Входящий номер заказчика')
    incoming_date = models.DateField(blank=True, null=True, verbose_name='Входящая дата заказчика')
    responsible_person_from_customer = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ответственный от заказчика')
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сделка')

    def __str__(self):
        return f"Письмо №{self.incoming_number} от {self.customer.name_of_company}"

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
        ordering = ['-planned_date']


class Company_branch(models.Model):
    name_of_company = models.CharField(max_length=255, verbose_name='Название компании', null=False, blank=False, default='Без названия')
    revenue_for_last_year = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True,verbose_name='Выручка за последний год', help_text='Миллиард рублей')
    length_of_electrical_network_km = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Длина сетей, км')
    quantity_of_technical_transformer_pcs = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество ТП, шт')
    address = models.TextField(blank=True, null=True, verbose_name='Адрес')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='branches', blank=True, null=True, verbose_name='Родительский заказчик')

    def __str__(self):
        return self.name_of_company

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиал'
        ordering = ['name_of_company']