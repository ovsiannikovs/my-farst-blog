from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_file_size(value):
    """Ограничение файла 50 МБ"""
    limit = 50 * 1024 * 1024  # 50 MB
    if value.size > limit:
        raise ValidationError('Размер файла не должен превышать 50 МБ')


class SharedRepository(models.Model):
    """
    Сущность "Общий репозиторий" с функцией "Добавить документ"
    """

    # 1. Уникальный идентификатор
    id = models.AutoField(
        primary_key=True,
        verbose_name='Уникальный идентификатор'
    )

    # 2. Название документа
    document_title = models.CharField(
        max_length=100,
        verbose_name='Название документа',
        unique=True,
        help_text='Все текстовые символы - 100 символов max'
    )

    # 3. Создатель (автор)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='authored_documents',
        verbose_name='Создатель (автор)',
        help_text='Имя пользователя системы (ссылка на User)'
    )

    # 4. Дата и время создания
    date_of_creation = models.DateTimeField(
        verbose_name='Дата и время создания',
        default=timezone.now,
        help_text='Формат: YYYY-MM-DD HH:MI:SS'
    )

    # 5. Последний редактор
    last_editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='last_edited_documents',
        verbose_name='Последний редактор',
        help_text='Имя пользователя системы (ссылка на User)'
    )

    # 6. Дата и время последнего изменения
    date_of_change = models.DateTimeField(
        verbose_name='Дата и время последнего изменения',
        auto_now=True,
        help_text='Формат: YYYY-MM-DD HH:MI:SS'
    )

    # 7. Текущий ответственный
    current_responsible = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='responsible_documents',
        verbose_name='Текущий ответственный',
        help_text='Имя пользователя системы (ссылка на User)'
    )

    # 8. Версия
    version = models.CharField(
        max_length=3,
        verbose_name='Версия',
        default='1',
        help_text='Цифры, 3 символа max'
    )

    # 9. Загружаемый файл
    uploaded_file = models.FileField(
        upload_to='shared_repository/documents/%Y/%m/%d/',
        verbose_name='Загружаемый файл',
        validators=[validate_file_size],
        help_text='Текст, строго в соответствии с данными в колонке "Визуализация"'
    )

    # 10. Назначение документа
    document_purpose = models.TextField(
        max_length=5000,
        verbose_name='Назначение документа',
        blank=True,
        null=True,
        help_text='Все текстовые символы - 5000 символов max'
    )

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['-date_of_creation']

    def __str__(self):
        return f"{self.document_title} (v{self.version})"

    def save(self, *args, **kwargs):
        """Автоматическая установка полей при сохранении"""
        if not self.pk:  # Если это новый документ
            # Для нового документа автор = текущий ответственный = последний редактор
            self.author = self.current_responsible
            self.last_editor = self.current_responsible
            # Дата создания устанавливается автоматически через default=timezone.now
        else:  # Редактирование существующего
            # При редактировании обновляем последнего редактора
            # (date_of_change обновляется автоматически через auto_now=True)
            pass

        # Проверяем версию - должна содержать только цифры
        if self.version:
            self.version = ''.join(filter(str.isdigit, self.version))[:3]

        super().save(*args, **kwargs)

    def clean(self):
        """Валидация модели"""
        # Проверка версии - только цифры
        if self.version and not self.version.isdigit():
            raise ValidationError({
                'version': 'Версия должна содержать только цифры'
            })

        # Проверка длины версии
        if len(self.version) > 3:
            raise ValidationError({
                'version': 'Версия не должна превышать 3 символов'
            })