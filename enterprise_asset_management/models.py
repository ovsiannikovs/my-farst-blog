from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


MAX_FILE_MB = 50


def validate_file_size(value):
    limit = MAX_FILE_MB * 1024 * 1024
    if value.size > limit:
        raise ValidationError(f"Размер одного файла не должен превышать {MAX_FILE_MB} МБ")


class WorkEquipment(models.Model):
    """
    Рабочее оборудование
    """

    name_type = models.CharField("Наименование, тип", max_length=100)
    serial_number = models.CharField("Заводской номер (s/n)", max_length=12, blank=True, null=True,unique=True)
    measuring_device = models.BooleanField("Средство измерений", default=False)
    next_calibration_date = models.DateField("Дата плановой поверки", blank=True, null=True)
    workstation = models.CharField("Рабочее место", max_length=100, blank=True, null=True)

    replacement_allowed = models.CharField(
        "Допустимая замена",
        max_length=200,
        blank=True,
        null=True,
    )

    note = models.CharField(
        "Примечание",
        max_length=300,
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="work_equipment_author",
        verbose_name="Создатель (автор)",
    )
    date_of_creation = models.DateTimeField("Дата и время создания", default=timezone.now)

    last_editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="work_equipment_last_editor",
        verbose_name="Последний редактор",
    )
    date_of_change = models.DateTimeField("Дата и время последнего изменения", auto_now=True)

    current_responsible = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="work_equipment_current_responsible",
        verbose_name="Текущий ответственный",
    )

    version = models.CharField(
        "Версия",
        max_length=3,
        default="1",
    )
    version_diff = models.CharField("Сравнение версий", max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = "Рабочее оборудование"
        verbose_name_plural = "Рабочее оборудование"

    def clean(self):
        if self.measuring_device and not self.next_calibration_date:
            raise ValidationError({"next_calibration_date": "Обязательное поле для средства измерений."})

    def __str__(self):
        return self.name_type


class WorkEquipmentFile(models.Model):
    """
    Сопроводительные документы к рабочему оборудованию
    """

    work_equipment = models.ForeignKey(
        WorkEquipment,
        on_delete=models.CASCADE,
        related_name="files",
        verbose_name="Рабочее оборудование",
    )
    file = models.FileField("Файл", upload_to="work_equipment_files/", validators=[validate_file_size])
    uploaded_at = models.DateTimeField("Дата загрузки", default=timezone.now)

    class Meta:
        verbose_name = "Сопроводительный документ"
        verbose_name_plural = "Сопроводительные документы"

    def __str__(self):
        return f"Файл для: {self.work_equipment}"


class TransportVehicle(models.Model):
    """
    Транспортные средства
    """
    name = models.CharField("Наименование", max_length=100, unique=True)

    class Meta:
        verbose_name = "Транспортные средства"
        verbose_name_plural = "Транспортные средства"

    def __str__(self):
        return self.name


class Infrastructure(models.Model):
    """
    Инфраструктура
    """
    name = models.CharField("Наименование", max_length=100, unique=True)

    class Meta:
        verbose_name = "Инфраструктура"
        verbose_name_plural = "Инфраструктура"

    def __str__(self):
        return self.name
