from django.apps import AppConfig


class SharedRepositoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shared_repository'
    verbose_name = 'Управление общими документами'