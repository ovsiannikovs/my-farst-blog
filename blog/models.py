from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Заглушки / вспомогательные модели
class TechnicalAssignment(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): return self.title

class DesignDocumentation(models.Model):
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
    name = models.CharField(max_length=100)
    design_product = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_posts')
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='edited_posts')
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='responsible_posts')
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_change = models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=20)
    version_diff = models.TextField(max_length=1000, blank=True)
    litera = models.CharField(max_length=20)
    trl = models.CharField(max_length=10)

    # Связи
    technical_assignments = models.ManyToManyField(TechnicalAssignment, blank=True)
    design_documentation = models.OneToOneField(DesignDocumentation, on_delete=models.SET_NULL, null=True, blank=True)
    working_documentation = models.OneToOneField(WorkingDocumentation, on_delete=models.SET_NULL, null=True, blank=True)
    pilot_samples = models.OneToOneField(PilotSample, on_delete=models.SET_NULL, null=True, blank=True)
    procurement = models.ManyToManyField(Procurement, blank=True)
    production_launch = models.OneToOneField(ProductionLaunch, on_delete=models.SET_NULL, null=True, blank=True)
    production = models.OneToOneField(Production, on_delete=models.SET_NULL, null=True, blank=True)
    sales = models.OneToOneField(Sales, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.OneToOneField(Service, on_delete=models.SET_NULL, null=True, blank=True)
    patenting = models.ManyToManyField(Patenting, blank=True)
    conformity_assessment = models.OneToOneField(ConformityAssessment, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Разработка"
        verbose_name_plural = "Разработки"

    def __str__(self):
        return self.name


# Вспомогательные сущности для TechnicalProposal
class GeneralDrawingProduct(models.Model):
    CATEGORY_CHOICES = [
    ('ВПТ', 'Ведомость технического предложения'),
    ('ВО', 'Чертеж общего вида изделия'),
    ('ЭМИ', 'Электронная модель изделия'),
    ('Э6', 'Схема электрическая общая'),
    ('ПО ПТ', 'Программное обеспечение. Техническое предложение'),
    ('ВО СЕ', 'Чертеж общего вида сборочной единицы'),
    ('ЭМ СЕ', 'Электронная модель сборочной единицы'),
    ('ЧД СЕ', 'Чертеж детали сборочной единицы'),
    ('ЭМД СЕ', 'Электронная модель детали сборочной единицы'),
    ('ЧД ВО', 'Чертеж детали изделия'),
    ('ЭМД ВО', 'Электронная модель детали изделия'),
    ('ПЗ ПТ', 'Пояснительная записка. Техническое предложение'),
    ('ПЗ ПТ. Приложение', 'Пояснительная записка. Техническое предложение. Приложение'),
    ('Протокол ПТ', 'Протокол. Техническое предложение'),
]


    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ВО')
    name = models.CharField(max_length=100, default='ПАК СПМ 2.13 Чертеж общего вида изделия')
    desig_document = models.CharField(max_length=50, default='СИ.40522001.000.13ВО')
    info_format = models.CharField(max_length=20, default='ДЭ')
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ')
    change_number = models.CharField(max_length=50, default='Изм. 1')
    file = models.CharField(max_length=50, default='Autodesk Inventor (.idw)')
    application = models.CharField(max_length=50, default='Autodesk Inventor')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='gd_created_by')
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='gd_edited_by')
    date_of_change = models.DateTimeField(default=timezone.now)
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='gd_responsible')
    status = models.CharField(max_length=50, default='На согласовании')
    priority = models.CharField(max_length=30, blank=True, default='')
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(max_length=1000, blank=True, default='')
    litera = models.CharField(max_length=20, default='П-')
    trl = models.CharField(max_length=10, default='1-')
    validity_date = models.DateField(null=True, blank=True)
    subscribers = models.CharField(max_length=200, blank=True, default='')
    pattern = models.CharField(max_length=50, blank=True, default='ВО ПТ')
    develop_org = models.CharField(max_length=100, blank=True, default='ООО "СИСТЕМА"')
    language = models.CharField(max_length=10, blank=True, default='rus')
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self):
        return self.name
    def __str__(self): return self.name

class ElectronicModelProduct(models.Model):
    CATEGORY_CHOICES = [
        ('ВПТ', 'Ведомость технического предложения'),
        ('ВО', 'Чертеж общего вида изделия'),
        ('ЭМИ', 'Электронная модель изделия'),
    ]

    STATUS_CHOICES = [
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

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ЭМИ')
    name = models.CharField(max_length=100, default='ПАК СПМ 2.13 Электронная модель изделия')
    desig_document = models.CharField(max_length=50, unique=True, default='СИ.40522001.000.13ЭМИ')
    info_format = models.CharField(max_length=20, default='ДЭ')
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ')
    change_number = models.CharField(max_length=20, default='Изм. 1')
    file = models.CharField(max_length=50, default='Autodesk Inventor (.iam)')
    application = models.CharField(max_length=50, default='Autodesk Inventor')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='electronicmodel_author')
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='electronicmodel_last_editor')
    date_of_change = models.DateTimeField(default=timezone.now)
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='electronicmodel_responsible')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Рабочий вариант')
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, default='')
    approval_cycle = models.IntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(blank=True, default='')
    litera = models.CharField(max_length=20, default='П-')
    trl = models.CharField(max_length=10, choices=TRL_CHOICES, default='1-')
    validity_date = models.DateField(null=True, blank=True)
    subscribers = models.TextField(blank=True, default='')
    related_docs = models.TextField(blank=True, default='', verbose_name='Связанные сопроводительные документы')
    pattern = models.CharField(max_length=50, blank=True, default='ЭМИ ПТ')
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"')
    language = models.CharField(max_length=10, default='rus')
    technical_proposal = models.OneToOneField('TechnicalProposal', on_delete=models.CASCADE,default=1, related_name='electronic_model_product_link')

    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self):
        return self.name

class GeneralElectricalDiagram(models.Model):
    CATEGORY_CHOICES = [
        ('Э6', 'Схема электрическая общая'),
    ]

    INFO_FORMAT_CHOICES = [
        ('ДЭ', 'ДЭ'),
        ('ДЭ КД', 'ДЭ КД'),
        ('ТДЭ', 'ТДЭ'),
        ('ДБ КД', 'ДБ КД'),
    ]

    STATUS_CHOICES = [
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

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Э6')
    name = models.CharField(max_length=100, default='ПАК СПМ 2.13 Схема электрическая общая')
    desig_document = models.CharField(max_length=50, unique=True, default='СИ.40522001.000.13Э6')
    info_format = models.CharField(max_length=20, choices=INFO_FORMAT_CHOICES, default='ДЭ')
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ')
    change_number = models.CharField(max_length=20, default='Изм. 1')
    file = models.CharField(max_length=50, default='Autodesk AutoCAD (.dwg)')
    application = models.CharField(max_length=50, default='Autodesk AutoCAD')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    date_of_change = models.DateTimeField(default=timezone.now)
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='На согласовании')
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, default='')
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(blank=True, default='')
    litera = models.CharField(max_length=2, default='П-')
    trl = models.CharField(max_length=10, default='1-')
    validity_date = models.DateField(null=True, blank=True)
    subscribers = models.CharField(max_length=200, blank=True, default='')
    related_documents = models.TextField(blank=True, default='')
    pattern = models.CharField(max_length=50, blank=True, default='Э6 ПТ')
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"')
    language = models.CharField(max_length=10, default='rus')
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self):
        return self.name

class SoftwareProduct(models.Model):
    CATEGORY_CHOICES = [
        ('ПО ПТ', 'Программное обеспечение. Техническое предложение'),
    ]

    STATUS_CHOICES = [
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

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ПО ПТ')
    name = models.CharField(max_length=100, default='ПАК СПМ 2.13  Программное обеспечение. Техническое предложение')
    desig_document = models.CharField(max_length=50, unique=True, default='СИ.40522001.000.13ПО ПТ')
    info_format = models.CharField(max_length=30, default='ДЭ')
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ')
    change_number = models.CharField(max_length=20, default='Изм. 1')
    file = models.CharField(max_length=50, default='Microsoft Office Word (.docx)')
    application = models.CharField(max_length=50, default='Microsoft Office Word')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='software_author')
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='software_last_editor')
    date_of_change = models.DateTimeField(default=timezone.now)
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='software_responsible')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Рабочий вариант')
    priority = models.CharField(max_length=30, blank=True, default='')
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(max_length=1000, blank=True, default='')
    litera = models.CharField(max_length=20, default='П-')
    trl = models.CharField(max_length=10, default='1-')
    validity_date = models.DateField(null=True, blank=True)
    subscribers = models.CharField(max_length=200, blank=True, default='')
    related_documents = models.TextField(blank=True, default='')
    pattern = models.CharField(max_length=50, blank=True, default='ПО ПТ')
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"')
    language = models.CharField(max_length=10, default='rus')
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self):
        return self.name

class ReportTechnicalProposal(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    
    CATEGORY_CHOICES = [
        ("ПЗ ПТ", "Пояснительная записка. Техническое предложение"),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="ПЗ ПТ")

    name = models.CharField(max_length=100)
    desig_document = models.CharField(max_length=50, unique=True, null=True, blank=True)

    INFO_FORMAT_CHOICES = [
        ("ДБ", "ДБ КД"),
        ("ДЭ", "ДЭ КД"),
        ("ТДЭ", "ТДЭ"),
    ]
    info_format = models.CharField(max_length=10, choices=INFO_FORMAT_CHOICES, default="ДЭ", blank=True)

    primary_use = models.CharField(max_length=100, blank=True, null=True)

    file = models.CharField(max_length=50, default=0)
    application = models.CharField(max_length=100, default=0)

    author = models.ForeignKey(User, related_name='report_technical_proposal_authors', on_delete=models.SET_NULL, null=True)
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, related_name='report_technical_proposal_editors', on_delete=models.SET_NULL, null=True)
    date_of_change = models.DateTimeField(auto_now=True)
    current_responsible = models.ForeignKey(User, related_name='report_technical_proposal_responsibles', on_delete=models.SET_NULL, null=True)

    STATUS_CHOICES = [
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
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Рабочий вариант')

    PRIORITY_CHOICES = [
        ('Срочно', 'Срочно'),
        ('Высокий', 'Высокий'),
        ('Средний', 'Средний'),
        ('Низкий', 'Низкий'),
    ]
    priority = models.CharField(max_length=30, blank=True, null=True, choices=PRIORITY_CHOICES)

    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(max_length=1000, blank=True, null=True)

    litera = models.CharField(max_length=20, default='П-', editable=False)

    trl = models.CharField(max_length=10, default='1-', editable=False)

    validity_date = models.DateField(null=True, blank=True)
    subscribers = models.CharField(max_length=200, blank=True, null=True)
    related_documents = models.TextField(blank=True, null=True)
    pattern = models.CharField(max_length=50, blank=True, null=True, default='ПЗ ПТ')

    DEVELOP_ORG_CHOICES = [
        ('ООО "СИСТЕМА"', 'ООО "СИСТЕМА"'),
    ]
    develop_org = models.CharField(max_length=100, choices=DEVELOP_ORG_CHOICES, default='ООО "СИСТЕМА"', blank=True)

    LANGUAGE_CHOICES = [
        ('rus', 'Русский'),
        ('eng', 'Английский'),
    ]   
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='rus', blank=True)

    ACCESS_LEVEL_CHOICES = [
        ('О', 'Общий'),
        ('К', 'Конфиденциально'),
        ('С', 'Секретно'),
        ('СС', 'Совершенно секретно'),
    ]
    access_level = models.CharField(max_length=30, choices=ACCESS_LEVEL_CHOICES, default='О')

    PERMISSION_LEVEL_CHOICES = [
        ('0', 'Ничего не разрешено'),
        ('1', 'Исполнение'),
        ('2', 'Запись'),
        ('3', 'Запись и исполнение'),
        ('4', 'Чтение'),
        ('5', 'Чтение и исполнение'),
        ('6', 'Чтение и запись'),
        ('7', 'Чтение, запись и исполнение'),
    ]
    permission = models.CharField(max_length=2, choices=PERMISSION_LEVEL_CHOICES, default='7')
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self):
        return self.name or f"Пояснительная записка {self.desig_document}"

class ProtocolTechnicalProposal(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    
    category = models.CharField(
        max_length=100,
        default="Протокол ПТ",
        help_text="Категория документа"
    )
    name = models.CharField(max_length=100)
    desig_document = models.CharField(max_length=50, blank=True, null=True, unique=True)
    info_format = models.CharField(max_length=20, default="ДЭ", blank=True)
    primary_use = models.CharField(max_length=100, blank=True)

    file = models.CharField(max_length=50, blank=True)
    application = models.CharField(max_length=50, blank=True)

    author = models.ForeignKey(User, related_name='protocol_created', on_delete=models.SET_NULL, null=True)
    last_editor = models.ForeignKey(User, related_name='protocol_edited', on_delete=models.SET_NULL, null=True)
    current_responsible = models.ForeignKey(User, related_name='protocol_responsible', on_delete=models.SET_NULL, null=True)

    date_of_creation = models.DateTimeField(default=timezone.now)
    date_of_change = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=30, default='На согласовании')
    priority = models.CharField(max_length=30, blank=True)
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(max_length=1000, blank=True)

    litera = models.CharField(max_length=20, default='П-', editable=False)
    trl = models.CharField(max_length=10, default='1-')

    validity_date = models.DateField(blank=True, null=True)
    subscribers = models.CharField(max_length=200, blank=True)
    related_documents = models.TextField(blank=True)

    pattern = models.CharField(max_length=100, blank=True, default='Протокол ПТ')
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', blank=True)
    language = models.CharField(max_length=10, default='rus', blank=True)

    permission = models.CharField(max_length=50, default='7')
    access_level = models.CharField(max_length=30, default='О')

    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    class Meta:
        verbose_name = "Протокол. Техническое предложение"
        verbose_name_plural = "Протоколы. Технические предложения"

    def __str__(self):
        return f"{self.name} — {self.version}"

class GeneralDrawingUnit(models.Model):
    CATEGORY_CHOICES = [
        ('ВО СЕ', 'Чертеж общего вида сборочной единицы'),
    ]
    INFO_FORMAT_CHOICES = [
        ('ДЭ КД', 'Электронный конструкторский документ'),
        ('ДЭ', 'Электронный документ'),
    ]
    STATUS_CHOICES = [
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

    technical_proposal = models.ForeignKey('TechnicalProposal', on_delete=models.CASCADE, related_name='general_drawing_units')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ВО СЕ')
    name = models.CharField(max_length=100)
    desig_document = models.CharField(max_length=50, unique=True)
    info_format = models.CharField(max_length=20, choices=INFO_FORMAT_CHOICES, default='ДЭ')
    primary_use = models.CharField(max_length=100)
    change_number = models.CharField(max_length=20)
    file = models.CharField(max_length=50)
    application = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
    date_of_creation = models.DateTimeField(auto_now_add=True)
    last_editor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
    date_of_change = models.DateTimeField(auto_now=True)
    current_responsible = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Рабочий вариант')
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, null=True)
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(blank=True)
    litera = models.CharField(max_length=2, default='П-')
    trl = models.CharField(max_length=10, choices=TRL_CHOICES, default='1-')
    validity_date = models.DateField(blank=True, null=True)
    subscribers = models.TextField(blank=True)
    related_documents = models.TextField(blank=True)
    pattern = models.CharField(max_length=50, blank=True)
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"')
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='rus')
    access_rights = models.CharField(max_length=50, default='7')  # по умолчанию "Чтение, запись и исполнение"
    access_level = models.CharField(max_length=30, choices=ACCESS_LEVEL_CHOICES, default='О')
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self):
        return self.name

class ElectronicModelUnit(models.Model):
    CATEGORY_CHOICES = [
        ('ЭМ СЕ', 'Электронная модель сборочной единицы'),
    ]
    INFO_FORMAT_CHOICES = [
        ('ДЭ КД', 'Электронный конструкторский документ'),
        ('ДЭ', 'Электронный документ'),
    ]
    STATUS_CHOICES = [
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

    technical_proposal = models.ForeignKey('TechnicalProposal', on_delete=models.CASCADE, related_name='electronic_model_units', null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ЭМ СЕ')
    name = models.CharField(max_length=100, default='Узел 1 Электронная модель сборочной единицы')
    desig_document = models.CharField(max_length=50, unique=True, default=1)
    info_format = models.CharField(max_length=20, choices=INFO_FORMAT_CHOICES, default='ДЭ')
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ')
    change_number = models.CharField(max_length=20, default='Изм. 1')
    file = models.CharField(max_length=50, default='Autodesk Inventor (.iam)')
    application = models.CharField(max_length=100, default='Autodesk Inventor')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', default=1)
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', default=1)
    date_of_change = models.DateTimeField(auto_now=True)
    current_responsible = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', default=1)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Рабочий вариант')
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, null=True)
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(blank=True, default='')
    litera = models.CharField(max_length=2, default='П-')
    trl = models.CharField(max_length=10, choices=TRL_CHOICES, default='1-')
    validity_date = models.DateField(blank=True, null=True)
    subscribers = models.TextField(blank=True, default='')
    related_documents = models.TextField(blank=True, default='')
    pattern = models.CharField(max_length=50, blank=True, default='ЭМ СЕ ПТ')
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"')
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='rus')
    access_rights = models.CharField(max_length=50, default='7')
    access_level = models.CharField(max_length=30, choices=ACCESS_LEVEL_CHOICES, default='О')
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self):
        return self.name



class DrawingPartUnit(models.Model):
    CATEGORY_CHOICES = [
        ('ЧД СЕ', 'Чертеж детали сборочной единицы'),
    ]
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

    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='ЧД СЕ')
    name = models.CharField(max_length=100)
    desig_document = models.CharField(max_length=50, unique=True, default='1')
    info_format = models.CharField(max_length=10, choices=INFO_FORMAT_CHOICES, default='ДЭ')
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ')
    change_number = models.CharField(max_length=20, default='Изм. 1')
    file = models.CharField(max_length=50, default='Autodesk Inventor (.idw)')
    application = models.CharField(max_length=50, default='Autodesk Inventor')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='drawing_partunit_author')
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='drawing_partunit_editor')
    date_of_change = models.DateTimeField(default=timezone.now)
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='drawing_partunit_responsible')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='На согласовании')
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, null=True)
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(max_length=1000, blank=True)
    litera = models.CharField(max_length=2, default='П-')
    trl = models.CharField(max_length=10, default='1-')
    validity_date = models.DateField(blank=True, null=True)
    subscribers = models.TextField(max_length=200, blank=True)
    related_documents = models.TextField(blank=True)
    pattern = models.CharField(max_length=50, blank=True, default='ЧД СЕ ПТ')
    develop_org = models.CharField(max_length=50, default='ООО "СИСТЕМА"')
    language = models.CharField(max_length=10, default='rus')
    technical_proposal = models.ForeignKey('TechnicalProposal', on_delete=models.CASCADE, related_name='drawing_part_units', null=True)
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self):
        return self.name

class ElectronicModelPartUnit(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(default='ЭМД СЕ', max_length=100)
    name = models.CharField(max_length=100)
    desig_document = models.CharField(max_length=50, unique=True, default=1)
    info_format = models.CharField(max_length=50, default='ДЭ')
    primary_use = models.CharField(max_length=100, default='СИ.40522001.000.13ВПТ')
    change_number = models.CharField(max_length=50, default='Изм. 1')
    file = models.CharField(max_length=50, blank=True, null=True)
    application = models.CharField(max_length=50, default='Autodesk Inventor')
    author = models.ForeignKey(User, related_name='electronic_model_part_units_created', on_delete=models.PROTECT, null=True)
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, related_name='electronic_model_part_units_edited', on_delete=models.PROTECT, null=True)
    date_of_change = models.DateTimeField(default=timezone.now)
    current_responsible = models.ForeignKey(User, related_name='electronic_model_part_units_responsible', on_delete=models.PROTECT, null=True)
    status = models.CharField(max_length=50, default='На согласовании')
    priority = models.CharField(max_length=30, blank=True, null=True)
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(blank=True, null=True)
    litera = models.CharField(max_length=20, default='П-')
    trl = models.CharField(max_length=10, default='1-')
    validity_date = models.DateField(blank=True, null=True)
    subscribers = models.TextField(blank=True, null=True)
    related_documents = models.TextField(blank=True, null=True)
    pattern = models.CharField(max_length=50, default='ЭМД СЕ ПТ', blank=True, null=True)
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', blank=True, null=True)
    language = models.CharField(max_length=10, default='rus', blank=True, null=True)
    technical_proposal = models.ForeignKey('TechnicalProposal', on_delete=models.CASCADE, related_name='electronic_model_part_units', null=True)
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    class Meta:
        verbose_name = 'Электронная модель детали СЕ'
        verbose_name_plural = 'Электронные модели деталей СЕ'

    def __str__(self):
        return f"{self.desig_document} — {self.name}"

class DrawingPartProduct(models.Model):
    CATEGORY_CHOICES = [
        ("ЧД ВО", "Чертеж детали изделия"),
    ]
    INFO_FORMAT_CHOICES = [
        ("ДЭ", "ДЭ"),
        ("ДЭ КД", "ДЭ КД"),
        ("ТДЭ", "ТДЭ"),
        ("ДБ КД", "ДБ КД"),
    ]
    STATUS_CHOICES = [
        ("Рабочий вариант", "Рабочий вариант"),
        ("На согласовании", "На согласовании"),
        # и другие статусы
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

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="ЧД ВО")
    name = models.CharField(max_length=100)
    desig_document = models.CharField(max_length=50, unique=True, default=1)
    info_format = models.CharField(max_length=10, choices=INFO_FORMAT_CHOICES, default="ДЭ")
    primary_use = models.CharField(max_length=100, default="СИ.40522001.000.13ВПТ")
    change_number = models.CharField(max_length=20, default="Изм. 1")
    file = models.CharField(max_length=50, blank=True)
    application = models.CharField(max_length=50, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="drawing_part_product_authors")
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="drawing_part_product_editors")
    date_of_change = models.DateTimeField(auto_now=True)
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="drawing_part_product_responsibles")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Рабочий вариант")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True)
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default="v1.0")
    version_diff = models.TextField(blank=True)
    litera = models.CharField(max_length=20, default="П-")
    trl = models.CharField(max_length=10, choices=TRL_CHOICES, default="1-")
    validity_date = models.DateField(null=True, blank=True)
    subscribers = models.TextField(blank=True)
    pattern = models.CharField(max_length=50, blank=True, default="ЧД ВО ПТ")
    develop_org = models.CharField(max_length=100, default="ООО \"СИСТЕМА\"")
    language = models.CharField(max_length=10, default="rus")
    access_rights = models.CharField(max_length=50, default="7")
    access_level = models.CharField(max_length=10, choices=ACCESS_LEVEL_CHOICES, default="О")
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self):
        return f"{self.desig_document} — {self.name}"

class ElectronicModelPartProduct(models.Model):
    category = models.CharField(max_length=50, default="ЭМД ВО")
    name = models.CharField(max_length=100)
    desig_document = models.CharField(max_length=50, unique=True, default=1)
    info_format = models.CharField(max_length=20, default="ДЭ", blank=True)
    primary_use = models.CharField(max_length=100, blank=True)
    change_number = models.CharField(max_length=20, blank=True)
    file = models.CharField(max_length=50, blank=True)
    application = models.CharField(max_length=100, blank=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='empp_author', null=True)
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='empp_editor', null=True)
    date_of_creation = models.DateTimeField(default=timezone.now)
    date_of_change = models.DateTimeField(auto_now=True)
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='empp_responsible', null=True)

    status = models.CharField(max_length=30, default="Рабочий вариант")
    priority = models.CharField(max_length=30, blank=True)
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default="v1.0")
    version_diff = models.TextField(blank=True)
    litera = models.CharField(max_length=20, default="П-")
    trl = models.CharField(max_length=10, default="1-")
    validity_date = models.DateField(null=True, blank=True)
    subscribers = models.TextField(blank=True)
    related_documents = models.TextField(blank=True)
    pattern = models.CharField(max_length=100, blank=True)
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"', blank=True)
    language = models.CharField(max_length=10, default="rus", blank=True)
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self):
        return f"{self.desig_document} — {self.name}"

class AddReportTechnicalProposal(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)

    CATEGORY_CHOICES = [
        ("ПЗ ПТ. Приложение", "Пояснительная записка. Техническое предложение. Приложение"),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="ПЗ ПТ. Приложение")

    name = models.CharField(max_length=100)

    desig_document = models.CharField(max_length=50, unique=True, null=True, blank=True)

    INFO_FORMAT_CHOICES = [
        ("ДБ", "ДБ КД"),
        ("ДЭ", "ДЭ КД"),
        ("ТДЭ", "ТДЭ"),
    ]
    info_format = models.CharField(max_length=10, choices=INFO_FORMAT_CHOICES, default="ДЭ", blank=True)

    primary_use = models.CharField(max_length=100, blank=True, null=True)

    file = models.CharField(max_length=50, default=0)
    application = models.CharField(max_length=100, default=0)

    author = models.ForeignKey(User, related_name='add_report_authors', on_delete=models.SET_NULL, null=True)
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, related_name='add_report_editors', on_delete=models.SET_NULL, null=True)
    date_of_change = models.DateTimeField(auto_now=True)
    current_responsible = models.ForeignKey(User, related_name='add_report_responsibles', on_delete=models.SET_NULL, null=True)
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    STATUS_CHOICES = [
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
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Рабочий вариант')

    PRIORITY_CHOICES = [
        ('Срочно', 'Срочно'),
        ('Высокий', 'Высокий'),
        ('Средний', 'Средний'),
        ('Низкий', 'Низкий'),
    ]
    priority = models.CharField(max_length=30, blank=True, null=True, choices=PRIORITY_CHOICES)

    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(max_length=1000, blank=True, null=True)

    litera = models.CharField(max_length=20, default='П-', editable=False)
    trl = models.CharField(max_length=10, default='1-', editable=False)

    validity_date = models.DateField(null=True, blank=True)
    subscribers = models.CharField(max_length=200, blank=True, null=True)
    related_documents = models.TextField(blank=True, null=True)
    pattern = models.CharField(max_length=50, blank=True, null=True, default='ПЗ ПТ')

    DEVELOP_ORG_CHOICES = [
        ('ООО "СИСТЕМА"', 'ООО "СИСТЕМА"'),
    ]
    develop_org = models.CharField(max_length=100, choices=DEVELOP_ORG_CHOICES, default='ООО "СИСТЕМА"', blank=True)

    LANGUAGE_CHOICES = [
        ('rus', 'Русский'),
        ('eng', 'Английский'),
    ]
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='rus', blank=True)

    ACCESS_LEVEL_CHOICES = [
        ('О', 'Общий'),
        ('К', 'Конфиденциально'),
        ('С', 'Секретно'),
        ('СС', 'Совершенно секретно'),
    ]
    access_level = models.CharField(max_length=30, choices=ACCESS_LEVEL_CHOICES, default='О')

    PERMISSION_LEVEL_CHOICES = [
        ('0', 'Ничего не разрешено'),
        ('1', 'Исполнение'),
        ('2', 'Запись'),
        ('3', 'Запись и исполнение'),
        ('4', 'Чтение'),
        ('5', 'Чтение и исполнение'),
        ('6', 'Чтение и запись'),
        ('7', 'Чтение, запись и исполнение'),
    ]
    permission = models.CharField(max_length=2, choices=PERMISSION_LEVEL_CHOICES, default='7')

    def __str__(self):
        return self.name or f"ПЗ ПТ. Приложение {self.desig_document or self.id}"

class ListTechnicalProposal(models.Model):
    CATEGORY_CHOICES = [
        ('ВПТ', 'Ведомость технического предложения'),
        ('ВО', 'Чертеж общего вида изделия'),
        ('ЭМИ', 'Электронная модель изделия'),
    ]

    INFO_FORMAT_CHOICES = [
        ('ДБ КД', 'Бумажный КД'),
        ('ДЭ КД', 'Электронный КД'),
        ('ТДЭ', 'Текстовый электронный документ'),
    ]

    STATUS_CHOICES = [
        ('Рабочий вариант', 'Рабочий вариант'),
        ('Разработка', 'Разработка'),
        ('На согласовании', 'На согласовании'),
        ('Утвержден', 'Утвержден'),
    ]

    PRIORITY_CHOICES = [
        ('Срочно', 'Срочно'),
        ('Высокий', 'Высокий'),
        ('Средний', 'Средний'),
        ('Низкий', 'Низкий'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ВПТ')
    name = models.CharField(max_length=100, default='Ведомость ТП')
    desig_document = models.CharField(max_length=50, unique=True, default=1)
    info_format = models.CharField(max_length=20, choices=INFO_FORMAT_CHOICES, default='ДЭ')
    primary_use = models.CharField(max_length=100, default='Нет данных')
    change_number = models.CharField(max_length=20, default='Изм. 0')
    file = models.CharField(max_length=50, default='Файл не указан')
    application = models.CharField(max_length=50, default='Приложение не указано')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_list_tp')
    date_of_creation = models.DateTimeField(default=timezone.now)
    last_editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='edited_list_tp')
    date_of_change = models.DateTimeField(default=timezone.now)
    current_responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='responsible_list_tp')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Рабочий вариант')
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, blank=True, default='')
    approval_cycle = models.PositiveSmallIntegerField(default=0)
    version = models.CharField(max_length=6, default='v1.0')
    version_diff = models.TextField(blank=True, default='')
    litera = models.CharField(max_length=20, default='П-')
    trl = models.CharField(max_length=10, default='1-')
    validity_date = models.DateField(null=True, blank=True)
    subscribers = models.TextField(blank=True, default='')
    pattern = models.CharField(max_length=50, blank=True, default='ВПТ')
    develop_org = models.CharField(max_length=100, default='ООО "СИСТЕМА"')
    language = models.CharField(max_length=10, default='rus')
    uploaded_file = models.FileField(upload_to='uploads/', default=0)

    def __str__(self): return self.name


# Модель TechnicalProposal
class TechnicalProposal(models.Model):
    name = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, related_name='tp_created_by', on_delete=models.SET_NULL, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    last_editor = models.ForeignKey(User, related_name='tp_last_edited_by', on_delete=models.SET_NULL, null=True)
    date_of_change = models.DateTimeField(auto_now=True)
    current_responsible = models.ForeignKey(User, related_name='tp_current_responsible', on_delete=models.SET_NULL, null=True)
    version = models.CharField(max_length=20, blank=True)
    version_diff = models.TextField(max_length=1000, blank=True)
    litera = models.CharField(max_length=20, default='П-')
    trl = models.CharField(max_length=10, default='1-')

    list_technical_proposal = models.OneToOneField(ListTechnicalProposal, on_delete=models.SET_NULL, null=True, blank=True)
    general_drawing_product = models.OneToOneField(GeneralDrawingProduct, on_delete=models.SET_NULL, null=True, blank=True)
    electronic_model_product = models.OneToOneField(ElectronicModelProduct, on_delete=models.SET_NULL, null=True, blank=True)
    general_electrical_diagram = models.OneToOneField(GeneralElectricalDiagram, on_delete=models.SET_NULL, null=True, blank=True)
    software_product = models.OneToOneField(SoftwareProduct, on_delete=models.SET_NULL, null=True, blank=True)
    report_technical_proposal = models.OneToOneField(ReportTechnicalProposal, on_delete=models.SET_NULL, null=True, blank=True)
    protocol_technical_proposal = models.OneToOneField(ProtocolTechnicalProposal, on_delete=models.SET_NULL, null=True, blank=True)

    general_drawing_unit = models.ManyToManyField(GeneralDrawingUnit, blank=True)
    electronic_model_unit = models.ManyToManyField(ElectronicModelUnit, blank=True)
    drawing_part_unit = models.ManyToManyField(DrawingPartUnit, blank=True)
    electronic_model_part_unit = models.ManyToManyField(ElectronicModelPartUnit, blank=True)
    drawing_part_product = models.ManyToManyField(DrawingPartProduct, blank=True)
    electronic_model_part_product =  models.ManyToManyField(ElectronicModelPartProduct, blank=True)
    add_report_technical_proposal = models.ManyToManyField(AddReportTechnicalProposal, blank=True)

    class Meta:
        verbose_name = "Техническое предложение"
        verbose_name_plural = "Технические предложения"

    def __str__(self):
        return self.name


