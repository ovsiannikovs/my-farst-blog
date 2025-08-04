from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class technical_design(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class prelim_design(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title    

class WorkingDocumentation(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class PilotSample(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Procurement(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class ProductionLaunch(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Production(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Sales(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Service(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class Patenting(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class ConformityAssessment(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title


# Модель Post
class Post(models.Model):
    LITERA_CHOICES = [
        ('П-', 'П-'),
        ('П', 'П'),
    ]

    TRL_CHOICES = [
        ('1-', '1-'),
        ('1', '1'),
    ]
    name = models.CharField(max_length=100, verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, verbose_name="Обозначение изделия")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_posts', verbose_name="Автор")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='edited_posts', verbose_name="Последний редактор")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='responsible_posts', verbose_name="Текущий ответственный")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    version = models.CharField(max_length=20, default='1', verbose_name="Версия")
    version_diff = models.TextField(max_length=1000, blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=20, choices=LITERA_CHOICES, default='П-', verbose_name="Стадия разработки (литера)")
    trl = models.CharField(max_length=10, choices=TRL_CHOICES, default='1-', verbose_name="Уровень готовности технологий (TRL)")

    # Связи
    technical_assignments = models.OneToOneField('TechnicalAssignment', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Технические задания")
    technical_proposal = models.OneToOneField('TechnicalProposal', on_delete=models.SET_NULL, blank=True, null=True, related_name='Post', verbose_name='Техническое предложение')
    prelim_design = models.OneToOneField(prelim_design, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Эскизный проект")
    technical_design = models.OneToOneField(technical_design, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Технический проект")
    working_documentation = models.OneToOneField(WorkingDocumentation, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Рабочая КД")
    pilot_samples = models.OneToOneField(PilotSample, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Опытные образцы")
    procurement = models.ManyToManyField(Procurement, blank=True, verbose_name="Закупки")
    production_launch = models.OneToOneField(ProductionLaunch, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Постановка на производство")
    production = models.OneToOneField(Production, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Производство")
    sales = models.OneToOneField(Sales, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Продажи")
    service = models.OneToOneField(Service, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Сервисное обслуживание")
    patenting = models.ManyToManyField(Patenting, blank=True, verbose_name="Патентование")
    conformity_assessment = models.OneToOneField(ConformityAssessment, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Подтверждение соответствия")

    class Meta:
        verbose_name = "Разработка"
        verbose_name_plural = "Разработки"

    def __str__(self):
        return self.name


# Вспомогательные сущности для TechnicalProposal
class GeneralDrawingProduct(models.Model):


    category = models.CharField(max_length=50, default='ВО', verbose_name="Категория")
    name = models.CharField(max_length=100, default='ПАК СПМ 2.13 Чертеж общего вида изделия', verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, default='СИ.40522001.000.13ВО', verbose_name="Обозначение документа")
    info_format = models.CharField(max_length=20, default='ДЭ', verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='gd_created_by', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='gd_edited_by', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='gd_responsible', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=50, default='На согласовании', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(max_length=1000, blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=20, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(max_length=1000,blank=True,default='',verbose_name="Связанные сопроводительные документы")
    pattern = models.CharField(max_length=50, blank=True, default='ВО ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, blank=True, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, blank=True, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Чертеж общего вида изделия'
        verbose_name_plural = 'Чертежи общего вида изделия'
    def __str__(self):
        return self.name
    def __str__(self): return self.name

class ElectronicModelProduct(models.Model):

    STATUS_CHOICES = [
        ('Зарегистрирован', 'Зарегистрирован'),
        ('Рабочий вариант', 'Рабочий вариант'),
        ('Разработка', 'Разработка'),
        ('Проверка', 'Проверка'),
        ('Проверен', 'Проверен'),
        ('На согласовании', 'На согласовании'),
        ('Согласован', 'Согласован'),
        ('На утверждении', 'На утверждении'),
        ('Утвержден', 'Утвержден'),
        ('Отклонен', 'Отклонен'),
        ('Выпущен', 'Выпущен'),
        ('Заморожен', 'Заморожен'),
        ('Заменен', 'Заменен'),
        ('Заблокирован', 'Заблокирован'),
        ('Аннулирован', 'Аннулирован'),
        ('На пересмотре', 'На пересмотре'),
        ('Архив', 'Архив'),
    ]

    PRIORITY_CHOICES = [
        ('Срочно', 'Срочно'),
        ('Высокий', 'Высокий'),
        ('Средний', 'Средний'),
        ('Низкий', 'Низкий'),
    ]

    TRL_CHOICES = [
        ('1', '1'), ('2-', '2-'), ('2', '2'), ('3-', '3-'), ('3', '3'),
    ]

    category = models.CharField(max_length=50, default='ЭМИ', verbose_name="Категория")
    name = models.CharField(max_length=100, default='ПАК СПМ 2.13 Электронная модель изделия', verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, unique=True, default='СИ.40522001.000.13ЭМИ', verbose_name="Обозначение документа")
    info_format = models.CharField(max_length=20, default='ДЭ', verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    change_number = models.CharField(max_length=20, default='Изм. 1', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='electronicmodel_author', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='electronicmodel_last_editor', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='electronicmodel_responsible', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=20, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, choices=TRL_CHOICES, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.TextField(blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_docs = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='ЭМИ ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")

    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Электронная модель продукта'
        verbose_name_plural = 'Электронные модели продукта'
    def __str__(self):
        return self.name

class GeneralElectricalDiagram(models.Model):

    INFO_FORMAT_CHOICES = [
        ('ДЭ', 'ДЭ'),
        ('ДБ', 'ДБ'),
    ]

    STATUS_CHOICES = [
        ('Зарегистрирован', 'Зарегистрирован'),
        ('Рабочий вариант', 'Рабочий вариант'),
        ('Разработка', 'Разработка'),
        ('Проверка', 'Проверка'),
        ('Проверен', 'Проверен'),
        ('На согласовании', 'На согласовании'),
        ('Согласован', 'Согласован'),
        ('На утверждении', 'На утверждении'),
        ('Утвержден', 'Утвержден'),
        ('Отклонен', 'Отклонен'),
        ('Выпущен', 'Выпущен'),
        ('Заморожен', 'Заморожен'),
        ('Заменен', 'Заменен'),
        ('Заблокирован', 'Заблокирован'),
        ('Аннулирован', 'Аннулирован'),
        ('На пересмотре', 'На пересмотре'),
        ('Архив', 'Архив'),
    ]

    PRIORITY_CHOICES = [
        ('Срочно', 'Срочно'),
        ('Высокий', 'Высокий'),
        ('Средний', 'Средний'),
        ('Низкий', 'Низкий'),
    ]

    category = models.CharField(max_length=50, default='Э6', verbose_name="Категория")
    name = models.CharField(max_length=100, default='ПАК СПМ 2.13 Схема электрическая общая', verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, unique=True, default='СИ.40522001.000.13Э6', verbose_name="Обозначение документа")
    info_format = models.CharField(max_length=20, choices=INFO_FORMAT_CHOICES, default='ДЭ', verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    change_number = models.CharField(max_length=20, default='Изм. 1', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Схема электрическая общая'
        verbose_name_plural = 'Схемы электрические общие'
    def __str__(self):
        return self.name

class SoftwareProduct(models.Model):

    STATUS_CHOICES = [
        ('Зарегистрирован', 'Зарегистрирован'),
        ('Рабочий вариант', 'Рабочий вариант'),
        ('Разработка', 'Разработка'),
        ('Проверка', 'Проверка'),
        ('Проверен', 'Проверен'),
        ('На согласовании', 'На согласовании'),
        ('Согласован', 'Согласован'),
        ('На утверждении', 'На утверждении'),
        ('Утвержден', 'Утвержден'),
        ('Отклонен', 'Отклонен'),
        ('Выпущен', 'Выпущен'),
        ('Заморожен', 'Заморожен'),
        ('Заменен', 'Заменен'),
        ('Заблокирован', 'Заблокирован'),
        ('Аннулирован', 'Аннулирован'),
        ('На пересмотре', 'На пересмотре'),
        ('Архив', 'Архив'),
    ]

    category = models.CharField(max_length=50, default='ПО ПТ', verbose_name="Категория")
    name = models.CharField(max_length=100, default='ПАК СПМ 2.13  Программное обеспечение. Техническое предложение', verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, unique=True, default='СИ.40522001.000.13ПО ПТ', verbose_name="Обозначение документа")
    info_format = models.CharField(max_length=30, default='ДЭ', verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    change_number = models.CharField(max_length=20, default='Изм. 1', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Программное обеспечение Технического предложения'
        verbose_name_plural = 'Программные обеспечения Технического предложения'
    def __str__(self):
        return self.name

class ReportTechnicalProposal(models.Model):

    category = models.CharField(max_length=50, default="ПЗ ПТ", verbose_name="Категория")

    name = models.CharField(max_length=100, verbose_name="Наименование")

    INFO_FORMAT_CHOICES = [
        ("ДБ", "ДБ"),
        ("ДЭ", "ДЭ"),
    ]
    info_format = models.CharField(max_length=10, choices=INFO_FORMAT_CHOICES, default="ДЭ", blank=True, verbose_name="Формат представления информации")

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True, related_name='+', verbose_name="Текущий ответственный")

    STATUS_CHOICES = [
        ('Зарегистрирован', 'Зарегистрирован'),
        ('В разработке', 'В разработке'),
        ('На проверке', 'На проверке'),
        ('На утверждении', 'На утверждении'),
        ('Выпущен', 'Выпущен'),
        ('Заменен', 'Заменен'),
        ('Аннулирован', 'Аннулирован'), 
        ('В архиве',  'В архиве')
        ]
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, null=True, verbose_name="Загружаемый файл")

    DEVELOP_ORG_CHOICES = [
        ('ООО "СИСТЕМА"', 'ООО "СИСТЕМА"'),
    ]
    develop_org = models.CharField(max_length=100, choices=DEVELOP_ORG_CHOICES, default='ООО "СИСТЕМА"', blank=True, verbose_name="Организация-разработчик")

    LANGUAGE_CHOICES = [
        ('rus', 'rus'),
        ('eng', 'eng'),
    ]   
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='rus', blank=True, verbose_name="Язык")

    uploaded_file = models.FileField(upload_to='uploads/', default=0, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Пояснительна записка Технического предложения'
        verbose_name_plural = 'Пояснительные записки Технического предложения'
    def __str__(self):
        return self.name

class ProtocolTechnicalProposal(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    
    category = models.CharField(
        max_length=100,
        default="Протокол ПТ",
        verbose_name="Категория"
    )
    name = models.CharField(max_length=100, verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name="Обозначение изделия")
    info_format = models.CharField(max_length=20, default="ДЭ", blank=True, verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    change_number = models.CharField(max_length=20, default='Изм. 1', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=30, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = "Протокол. Техническое предложение"
        verbose_name_plural = "Протоколы. Технические предложения"

    def __str__(self):
        return f"{self.name} — {self.version}"

class GeneralDrawingUnit(models.Model):

    INFO_FORMAT_CHOICES = [
        ('ДБ', 'ДБ'),
        ('ДЭ', 'ДЭ'),
    ]
    STATUS_CHOICES = [
        ('Зарегистрирован', 'Зарегистрирован'),
        ('Рабочий вариант', 'Рабочий вариант'),
        ('Разработка', 'Разработка'),
        ('Проверка', 'Проверка'),
        ('Проверен', 'Проверен'),
        ('На согласовании', 'На согласовании'),
        ('Согласован', 'Согласован'),
        ('На утверждении', 'На утверждении'),
        ('Утвержден', 'Утвержден'),
        ('Отклонен', 'Отклонен'),
        ('Выпущен', 'Выпущен'),
        ('Заморожен', 'Заморожен'),
        ('Заменен', 'Заменен'),
        ('Заблокирован', 'Заблокирован'),
        ('Аннулирован', 'Аннулирован'),
        ('На пересмотре', 'На пересмотре'),
        ('Архив', 'Архив'),
    ]
    PRIORITY_CHOICES = [
        ('Срочно', 'Срочно'),
        ('Высокий', 'Высокий'),
        ('Средний', 'Средний'),
        ('Низкий', 'Низкий'),
    ]
    TRL_CHOICES = [('1-', '1-'), ('2-', '2-'), ('2', '2'), ('3-', '3-'), ('3', '3')]
    LANGUAGE_CHOICES = [('rus', 'rus'), ('eng', 'eng')]
    ACCESS_LEVEL_CHOICES = [('О', 'общий'), ('К', 'конфиденциально'), ('С', 'секретно'), ('СС', 'совершенно секретно')]

    category = models.CharField(max_length=50, default='ВО СЕ', verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, unique=True, verbose_name="Обозначение изделия")
    info_format = models.CharField(max_length=20, choices=INFO_FORMAT_CHOICES, default='ДЭ', verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    change_number = models.CharField(max_length=20, default='Изм. 1', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Чертеж общего вида сборочной единицы'
        verbose_name_plural = 'Чертежи общего вида сборочной еденицы'
    def __str__(self):
        return self.name

class ElectronicModelUnit(models.Model):

    INFO_FORMAT_CHOICES = [
        ('ДЭ КД', 'Электронный конструкторский документ'),
        ('ДЭ', 'Электронный документ'),
    ]
    STATUS_CHOICES = [
        ('Зарегистрирован', 'Зарегистрирован'),
        ('Рабочий вариант', 'Рабочий вариант'),
        ('Разработка', 'Разработка'),
        ('Проверка', 'Проверка'),
        ('Проверен', 'Проверен'),
        ('На согласовании', 'На согласовании'),
        ('Согласован', 'Согласован'),
        ('На утверждении', 'На утверждении'),
        ('Утвержден', 'Утвержден'),
        ('Отклонен', 'Отклонен'),
        ('Выпущен', 'Выпущен'),
        ('Заморожен', 'Заморожен'),
        ('Заменен', 'Заменен'),
        ('Заблокирован', 'Заблокирован'),
        ('Аннулирован', 'Аннулирован'),
        ('На пересмотре', 'На пересмотре'),
        ('Архив', 'Архив'),
    ]
    PRIORITY_CHOICES = [
        ('Срочно', 'Срочно'),
        ('Высокий', 'Высокий'),
        ('Средний', 'Средний'),
        ('Низкий', 'Низкий'),
    ]
    TRL_CHOICES = [('1-', '1-'), ('2-', '2-'), ('2', '2'), ('3-', '3-'), ('3', '3')]
    LANGUAGE_CHOICES = [('rus', 'rus'), ('eng', 'eng')]
    ACCESS_LEVEL_CHOICES = [('О', 'общий'), ('К', 'конфиденциально'), ('С', 'секретно'), ('СС', 'совершенно секретно')]

    category = models.CharField(max_length=50, default='ЭМ СЕ', verbose_name="Категория")
    name = models.CharField(max_length=100, default='Узел 1 Электронная модель сборочной единицы', verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, unique=True, default=1, verbose_name="Обозначение изделия")
    info_format = models.CharField(max_length=20, choices=INFO_FORMAT_CHOICES, default='ДЭ', verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    change_number = models.CharField(max_length=20, default='Изм. 1', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Электронная модель сборочной единицы'
        verbose_name_plural = 'Электронные модели сборочной единицы'
    def __str__(self):
        return self.name



class DrawingPartUnit(models.Model):

    INFO_FORMAT_CHOICES = [
        ('ДЭ КД', 'Электронный конструкторский документ'),
        ('ДЭ', 'Электронный документ'),
    ]
    PRIORITY_CHOICES = [
        ('Срочно', 'Срочно'),
        ('Высокий', 'Высокий'),
        ('Средний', 'Средний'),
        ('Низкий', 'Низкий'),
    ]
    STATUS_CHOICES = [
        ('Зарегистрирован', 'Зарегистрирован'),
        ('Рабочий вариант', 'Рабочий вариант'),
        ('Разработка', 'Разработка'),
        ('Проверка', 'Проверка'),
        ('Проверен', 'Проверен'),
        ('На согласовании', 'На согласовании'),
        ('Согласован', 'Согласован'),
        ('На утверждении', 'На утверждении'),
        ('Утвержден', 'Утвержден'),
        ('Отклонен', 'Отклонен'),
        ('Выпущен', 'Выпущен'),
        ('Заморожен', 'Заморожен'),
        ('Заменен', 'Заменен'),
        ('Заблокирован', 'Заблокирован'),
        ('Аннулирован', 'Аннулирован'),
        ('На пересмотре', 'На пересмотре'),
        ('Архив', 'Архив'),
    ]

    category = models.CharField(max_length=20, default='ЧД СЕ', verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, unique=True, default='1', verbose_name="Обозначение изделия")
    info_format = models.CharField(max_length=10, choices=INFO_FORMAT_CHOICES, default='ДЭ', verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    change_number = models.CharField(max_length=20, default='Изм. 1', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Чертеж детали сборочной единицы'
        verbose_name_plural = 'Чертежи детали сборочной единицы'
    def __str__(self):
        return self.name

class ElectronicModelPartUnit(models.Model):
    category = models.CharField(default='ЭМД СЕ', max_length=100, verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, unique=True, default=1, verbose_name="Обозначение изделия")
    info_format = models.CharField(max_length=50, default='ДЭ', verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    change_number = models.CharField(max_length=20, default='Изм. 1', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=30, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Электронная модель детали СЕ'
        verbose_name_plural = 'Электронные модели деталей СЕ'

    def __str__(self):
        return f"{self.desig_document} — {self.name}"

class DrawingPartProduct(models.Model):

    INFO_FORMAT_CHOICES = [
        ("ДЭ", "ДЭ"),
        ("ДЭ КД", "ДЭ КД"),
        ("ТДЭ", "ТДЭ"),
        ("ДБ КД", "ДБ КД"),
    ]
    STATUS_CHOICES = [
        ('Зарегистрирован', 'Зарегистрирован'),
        ('Рабочий вариант', 'Рабочий вариант'),
        ('Разработка', 'Разработка'),
        ('Проверка', 'Проверка'),
        ('Проверен', 'Проверен'),
        ('На согласовании', 'На согласовании'),
        ('Согласован', 'Согласован'),
        ('На утверждении', 'На утверждении'),
        ('Утвержден', 'Утвержден'),
        ('Отклонен', 'Отклонен'),
        ('Выпущен', 'Выпущен'),
        ('Заморожен', 'Заморожен'),
        ('Заменен', 'Заменен'),
        ('Заблокирован', 'Заблокирован'),
        ('Аннулирован', 'Аннулирован'),
        ('На пересмотре', 'На пересмотре'),
        ('Архив', 'Архив'),
    ]
    PRIORITY_CHOICES = [
        ("Срочно", "Срочно"),
        ("Высокий", "Высокий"),
        ("Средний", "Средний"),
        ("Низкий", "Низкий"),
    ]
    TRL_CHOICES = [
        ("1-", "1-"), ("2-", "2-"), ("2", "2"), ("3-", "3-"), ("3", "3"),
    ]
    ACCESS_LEVEL_CHOICES = [
        ("О", "Общий"),
        ("К", "Конфиденциально"),
        ("С", "Секретно"),
        ("СС", "Совершенно секретно"),
    ]

    category = models.CharField(max_length=50, default="ЧД ВО", verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, unique=True, default=1, verbose_name="Обозначение изделия")
    info_format = models.CharField(max_length=10, choices=INFO_FORMAT_CHOICES, default="ДЭ", verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    change_number = models.CharField(max_length=20, default='Изм. 1', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Чертеж детали изделия'
        verbose_name_plural = 'Чертежи детали изделия'
    def __str__(self):
        return f"{self.desig_document} — {self.name}"

class ElectronicModelPartProduct(models.Model):
    category = models.CharField(max_length=50, default="ЭМД ВО", verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Наименование")
    desig_document = models.CharField(max_length=50, unique=True, default=1, verbose_name="Обозначение изделия")
    info_format = models.CharField(max_length=20, default="ДЭ", blank=True, verbose_name="Формат представления информации")
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ', verbose_name="Первичное применение")
    change_number = models.CharField(max_length=20, default='Изм. 1', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=30, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    class Meta:
        verbose_name = 'Электронная модель детали изделия'
        verbose_name_plural = 'Электронные модели детали изделия'
    def __str__(self):
        return f"{self.desig_document} — {self.name}"

class AddReportTechnicalProposal(models.Model):

    category = models.CharField(max_length=50, default="ПЗ ПТ. Приложение", verbose_name="Категория")

    name = models.CharField(max_length=100, verbose_name="Наименование")

    INFO_FORMAT_CHOICES = [
        ("ДБ", "ДБ КД"),
        ("ДЭ", "ДЭ КД"),
    ]
    info_format = models.CharField(max_length=10, choices=INFO_FORMAT_CHOICES, default="ДЭ", blank=True, verbose_name="Формат представления информации")


    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")

    STATUS_CHOICES = [
        ('Зарегистрирован', 'Зарегистрирован'),
        ('Рабочий вариант', 'Рабочий вариант'),
        ('Разработка', 'Разработка'),
        ('Проверка', 'Проверка'),
        ('Проверен', 'Проверен'),
        ('На согласовании', 'На согласовании'),
        ('Согласован', 'Согласован'),
        ('На утверждении', 'На утверждении'),
        ('Утвержден', 'Утвержден'),
        ('Отклонен', 'Отклонен'),
        ('Выпущен', 'Выпущен'),
        ('Заморожен', 'Заморожен'),
        ('Заменен', 'Заменен'),
        ('Заблокирован', 'Заблокирован'),
        ('Аннулирован', 'Аннулирован'),
        ('На пересмотре', 'На пересмотре'),
        ('Архив', 'Архив'),
    ]
    status = models.CharField(max_length=30, default='Зарегистрирован', verbose_name="Статус (состояние)")

    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")

    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")

    LANGUAGE_CHOICES = [
        ('rus', 'rus'),
        ('eng', 'eng'),
    ]
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='rus', verbose_name="Язык")

    class Meta:
        verbose_name = 'Приложение к пояснительной записке Технического предложения'
        verbose_name_plural = 'Приложения к пояснительным запискам Технического предложения'

    def __str__(self):
        return self.name or f"ПЗ ПТ. Приложение {self.desig_document or self.id}"

class ListTechnicalProposal(models.Model):

    INFO_FORMAT_CHOICES = [
        ('ДБ', 'ДБ'),
        ('ДЭ', 'ДЭ'),
    ]

    STATUS_CHOICES = [
        ('Зарегистрирован', 'Зарегистрирован'),
        ('В разработке', 'В разработке'),
        ('На проверке', 'На проверке'),
        ('На утверждении', 'На утверждении'),
        ('Выпущен', 'Выпущен'),
        ('Заменен', 'Заменен'),
        ('Аннулирован', 'Аннулирован'), 
        ('В архиве',  'В архиве')
        ]


    PRIORITY_CHOICES = [
        ('Срочно', 'Срочно'),
        ('Высокий', 'Высокий'),
        ('Средний', 'Средний'),
        ('Низкий', 'Низкий'),
    ]


    category = models.CharField(max_length=50, default='ВПТ', verbose_name="Категория")
    name = models.CharField(max_length=150, blank=True, verbose_name="Наименование")
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True, related_name='list_technical_proposals')
    desig_document = models.CharField(max_length=50, unique=True, default=1, verbose_name="Обозначение изделия")
    info_format = models.CharField(max_length=20, choices=INFO_FORMAT_CHOICES, default='ДЭ', verbose_name="Формат представления информации")
    change_number = models.CharField(max_length=20, default='без изм', verbose_name="Номер изменения")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+', verbose_name="Текущий ответственный")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Зарегистрирован', verbose_name="Статус (состояние)")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, default='', verbose_name="Приоритет в работе")
    version = models.CharField(max_length=6, default='1', verbose_name="Версия")
    version_diff = models.TextField(blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=2, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, default='1-', verbose_name="Уровень готовности технологий (TRL)")
    validity_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    subscribers = models.CharField(max_length=200, blank=True, default='', verbose_name="Внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ', verbose_name="Шаблон")
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', verbose_name="Организация-разработчик")
    language = models.CharField(max_length=10, default='rus', verbose_name="Язык")
    uploaded_file = models.FileField(upload_to='uploads/', blank = True, verbose_name="Загружаемый файл")


    class Meta:
        verbose_name = 'Ведомость технического предложения'
        verbose_name_plural = 'Ведомости технического предложения'


# Модель TechnicalProposal
class TechnicalProposal(models.Model):

    LITERA_CHOICES = [
        ('П-', 'П-'),
        ('П', 'П'),
    ]

    TRL_CHOICES = [
        ('1-', '1-'),
        ('1', '1'),
    ]
    name = models.CharField(max_length=200, unique=True, verbose_name="Категория")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, related_name='tp_last_edited_by', on_delete=models.SET_NULL, null=True, verbose_name="Последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, related_name='tp_current_responsible', on_delete=models.SET_NULL, null=True, verbose_name="Текущий ответственный")
    version = models.CharField(max_length=20, blank=True, default='1', verbose_name="Версия")
    version_diff = models.TextField(max_length=1000, blank=True, default='Стартовая версия', verbose_name="Сравнение версий")
    litera = models.CharField(max_length=20, choices=LITERA_CHOICES, default='П-', verbose_name="Стадия разработки  (Литера)")
    trl = models.CharField(max_length=10, choices=TRL_CHOICES, default='1-', verbose_name="Уровень готовности технологий (TRL)")

    list_technical_proposal = models.OneToOneField(ListTechnicalProposal, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ведомость технического предложения")
    general_drawing_product = models.OneToOneField(GeneralDrawingProduct, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Чертеж общего вида изделия")
    electronic_model_product = models.OneToOneField(ElectronicModelProduct, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Электронная модель изделия ")
    general_electrical_diagram = models.OneToOneField(GeneralElectricalDiagram, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Схема электрическая общая")
    software_product = models.OneToOneField(SoftwareProduct, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Программное обеспечение Технического предложения")
    report_technical_proposal = models.OneToOneField(ReportTechnicalProposal, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пояснительная записка ПЗ ПТ")
    protocol_technical_proposal = models.OneToOneField(ProtocolTechnicalProposal, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Протокол. Техническое предложение")

    general_drawing_unit = models.ManyToManyField(GeneralDrawingUnit, blank=True, verbose_name="Чертеж общего вида сборочной единицы")
    electronic_model_unit = models.ManyToManyField(ElectronicModelUnit, blank=True, verbose_name="Электронная модель сборочной единицы")
    drawing_part_unit = models.ManyToManyField(DrawingPartUnit, blank=True, verbose_name="Чертеж детали сборочной единицы")
    electronic_model_part_unit = models.ManyToManyField(ElectronicModelPartUnit, blank=True, verbose_name="Электронная модель детали сборочной единицы")
    drawing_part_product = models.ManyToManyField(DrawingPartProduct, blank=True, verbose_name="Чертеж детали изделия")
    electronic_model_part_product =  models.ManyToManyField(ElectronicModelPartProduct, blank=True, verbose_name="Электронная модель детали изделия")
    add_report_technical_proposal = models.ManyToManyField(AddReportTechnicalProposal, blank=True, verbose_name="ПЗ ПТ Приложение")

    class Meta:
        verbose_name = "Техническое предложение"
        verbose_name_plural = "Технические предложения"

    def __str__(self): return self.name



class TaskForDesignWork(models.Model):
    category = models.CharField(max_length=100, default="ТЗ ОКР", verbose_name="наименование")
    name = models.CharField(max_length=100, unique=True, verbose_name="категория")
    info_format = models.CharField(max_length=100, default="оригинал ДЭ", blank=True, null=True, verbose_name="формат предоставления информации")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_designtasks", verbose_name="автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="edited_designtasks", verbose_name="последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responsible_designtasks", verbose_name="текущий ответственный")
    status = models.CharField(max_length=50, default="Зарегистрирован", verbose_name="статус")
    priority = models.CharField(max_length=50, blank=True, null=True, verbose_name="приоритет")
    version = models.CharField(max_length=3, blank=True, null=True, verbose_name="версия")
    version_diff = models.TextField(max_length=1000, blank=True, null=True, verbose_name="разница версий")
    validity_date = models.DateField(blank=True, null=True, verbose_name="срок действия")
    subscribers = models.TextField(blank=True, null=True, verbose_name="внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, null=True, verbose_name="связанные сопроводительные документы")
    pattern = models.CharField(max_length=100, blank=True, null=True, verbose_name="шаблон")
    develop_org = models.CharField(max_length=100, blank=True, null=True, verbose_name="организация - разработчик")
    language = models.CharField(max_length=7, blank=True, null=True, verbose_name="язык")
    uploaded_file = models.FileField(upload_to='design_tasks/', blank=True, null=True, verbose_name="загружаемый файл")
    add_task_for_design_work = models.FileField(upload_to='design_tasks/add/', blank=True, null=True, verbose_name="приложение к ТЗ")
    plan_for_design_work = models.FileField(upload_to='design_tasks/plan/', blank=True, null=True, verbose_name="план работ по ТЗ")
    route = models.CharField(max_length=255,blank=True,null=True,verbose_name="Маршрут")

    class Meta:
        verbose_name = 'Техническое задание на ОКР'
        verbose_name_plural = 'Технические задания на ОКР'

    def __str__(self):
        return self.name


class RevisionTask(models.Model):
    category = models.CharField(max_length=100, default="ТЗ Д", verbose_name="категория")
    name = models.CharField(max_length=100, unique=True, verbose_name="наименование")
    info_format = models.CharField(max_length=100, default="оригинал ДЭ", blank=True, null=True, verbose_name="формат")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_revisions", verbose_name="автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="edited_revisions", verbose_name="последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responsible_revisions", verbose_name="текущий ответственный")
    status = models.CharField(max_length=50, default="Зарегистрирован", verbose_name="статус")
    priority = models.CharField(max_length=50, blank=True, null=True, verbose_name="приоритет")
    version = models.CharField(max_length=3, blank=True, null=True, verbose_name="версия")
    version_diff = models.TextField(max_length=1000, blank=True, null=True, verbose_name="разница версий")
    validity_date = models.DateField(blank=True, null=True, verbose_name="срок действия")
    subscribers = models.TextField(blank=True, null=True, verbose_name="внешние и внутренние получатели")
    related_documents = models.TextField(blank=True, null=True, verbose_name="связанный сопроводительные документы")
    pattern = models.CharField(max_length=100, blank=True, null=True, verbose_name="шаблон")
    develop_org = models.CharField(max_length=100, blank=True, null=True, verbose_name="организация - разработчик")
    language = models.CharField(max_length=7, blank=True, null=True, verbose_name="язык")
    uploaded_file = models.FileField(upload_to='revision_tasks/', blank=True, null=True, verbose_name="файл")
    add_task_for_revision = models.FileField(upload_to='revision_tasks/add/', blank=True, null=True, verbose_name="приложение к ТЗ")
    plan_for_revision = models.FileField(upload_to='revision_tasks/plan/', blank=True, null=True, verbose_name="план работ по ТЗ")
    route = models.CharField(max_length=255,blank=True,null=True,verbose_name="Маршрут")

    class Meta:
        verbose_name = 'Техническое задание на доработку'
        verbose_name_plural = 'Технические задания на доработку' 

    def __str__(self):
        return self.name


class WorkAssignment(models.Model):
    name = models.CharField(max_length=100, verbose_name="наименование")
    category = models.CharField(max_length=100, default="РЗ", verbose_name="категория")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="дата и время создания")
    last_editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="edited_workassignments", verbose_name="последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responsible_workassignments", verbose_name="текущий ответственный")
    version = models.CharField(max_length=3, blank=True, null=True, verbose_name="версия")
    task = models.TextField(verbose_name="задача")
    deadline = models.DateField(verbose_name="срок выполнения")
    result = models.CharField(max_length=100, verbose_name="результат")
    result_description = models.TextField(max_length=5000, blank=True, null=True, verbose_name="описание результата")
    route = models.CharField(max_length=255,blank=True,null=True,verbose_name="Маршрут")

    class Meta:
        verbose_name = 'Рабочее задание'
        verbose_name_plural = 'Рабочие задания'

    def __str__(self):
        return self.name

class TechnicalAssignment(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="наименование")
    author = models.ForeignKey(User, related_name='created_assignments', on_delete=models.CASCADE, verbose_name="автор")
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name="Дата и время создания")
    last_editor = models.ForeignKey(User, related_name='edited_assignments', on_delete=models.CASCADE, verbose_name="последний редактор")
    date_of_change = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего изменения")
    current_responsible = models.ForeignKey(User, related_name='responsible_assignments', on_delete=models.CASCADE, verbose_name="такущий ответственный")
    version = models.CharField(max_length=3, blank=True, null=True, verbose_name="версия")
    version_diff = models.TextField(max_length=1000, blank=True, null=True, verbose_name="разница версий")
    task_for_design_work = models.OneToOneField(TaskForDesignWork, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Техническое задание на ОКР")
    revision_task = models.OneToOneField(RevisionTask, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Техническое задание на доработку")
    work_assignment = models.OneToOneField(WorkAssignment, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Рабочие задания")
    route = models.CharField(max_length=255,blank=True,null=True,verbose_name="Маршрут")

    class AccessLevel(models.TextChoices):
        READ = '4', 'Чтение'
        WRITE = '2', 'Запись'
        EXECUTE = '1', 'Исполнение'
        FULL = '7', 'Чтение, запись и исполнение'

    access = models.CharField(max_length=1, choices=AccessLevel.choices, default=AccessLevel.FULL)

    class SecurityLevel(models.TextChoices):
        OPEN = 'О', 'Общий'
        CONFIDENTIAL = 'К', 'Конфиденциально'
        SECRET = 'С', 'Секретно'
        TOP_SECRET = 'СС', 'Совершенно секретно'

    security = models.CharField(max_length=2, choices=SecurityLevel.choices, default=SecurityLevel.OPEN)

    class Meta:
        verbose_name = 'Техническое задание'
        verbose_name_plural = 'Технические задания'

    def __str__(self):
        return self.name
