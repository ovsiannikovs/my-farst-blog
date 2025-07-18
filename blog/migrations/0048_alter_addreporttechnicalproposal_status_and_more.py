# Generated by Django 5.1.8 on 2025-07-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_remove_listtechnicalproposal_primary_use_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addreporttechnicalproposal',
            name='status',
            field=models.CharField(choices=[('Зарегистрирован', 'Зарегистрирован'), ('Рабочий вариант', 'Рабочий вариант'), ('Разработка', 'Разработка'), ('Проверка', 'Проверка'), ('Проверен', 'Проверен'), ('На согласовании', 'На согласовании'), ('Согласован', 'Согласован'), ('На утверждении', 'На утверждении'), ('Утвержден', 'Утвержден'), ('Отклонен', 'Отклонен'), ('Выпущен', 'Выпущен'), ('Заморожен', 'Заморожен'), ('Заменен', 'Заменен'), ('Заблокирован', 'Заблокирован'), ('Аннулирован', 'Аннулирован'), ('На пересмотре', 'На пересмотре'), ('Архив', 'Архив')], default='Зарегистрирован', max_length=50),
        ),
        migrations.AlterField(
            model_name='drawingpartproduct',
            name='status',
            field=models.CharField(choices=[('Зарегистрирован', 'Зарегистрирован'), ('Рабочий вариант', 'Рабочий вариант'), ('Разработка', 'Разработка'), ('Проверка', 'Проверка'), ('Проверен', 'Проверен'), ('На согласовании', 'На согласовании'), ('Согласован', 'Согласован'), ('На утверждении', 'На утверждении'), ('Утвержден', 'Утвержден'), ('Отклонен', 'Отклонен'), ('Выпущен', 'Выпущен'), ('Заморожен', 'Заморожен'), ('Заменен', 'Заменен'), ('Заблокирован', 'Заблокирован'), ('Аннулирован', 'Аннулирован'), ('На пересмотре', 'На пересмотре'), ('Архив', 'Архив')], default='Зарегистрирован', max_length=50),
        ),
        migrations.AlterField(
            model_name='drawingpartunit',
            name='status',
            field=models.CharField(choices=[('Зарегистрирован', 'Зарегистрирован'), ('Рабочий вариант', 'Рабочий вариант'), ('Разработка', 'Разработка'), ('Проверка', 'Проверка'), ('Проверен', 'Проверен'), ('На согласовании', 'На согласовании'), ('Согласован', 'Согласован'), ('На утверждении', 'На утверждении'), ('Утвержден', 'Утвержден'), ('Отклонен', 'Отклонен'), ('Выпущен', 'Выпущен'), ('Заморожен', 'Заморожен'), ('Заменен', 'Заменен'), ('Заблокирован', 'Заблокирован'), ('Аннулирован', 'Аннулирован'), ('На пересмотре', 'На пересмотре'), ('Архив', 'Архив')], default='Зарегистрирован', max_length=30),
        ),
        migrations.AlterField(
            model_name='electronicmodelproduct',
            name='status',
            field=models.CharField(choices=[('Зарегистрирован', 'Зарегистрирован'), ('Рабочий вариант', 'Рабочий вариант'), ('Разработка', 'Разработка'), ('Проверка', 'Проверка'), ('Проверен', 'Проверен'), ('На согласовании', 'На согласовании'), ('Согласован', 'Согласован'), ('На утверждении', 'На утверждении'), ('Утвержден', 'Утвержден'), ('Отклонен', 'Отклонен'), ('Выпущен', 'Выпущен'), ('Заморожен', 'Заморожен'), ('Заменен', 'Заменен'), ('Заблокирован', 'Заблокирован'), ('Аннулирован', 'Аннулирован'), ('На пересмотре', 'На пересмотре'), ('Архив', 'Архив')], default='Зарегистрирован', max_length=50),
        ),
        migrations.AlterField(
            model_name='electronicmodelunit',
            name='status',
            field=models.CharField(choices=[('Зарегистрирован', 'Зарегистрирован'), ('Рабочий вариант', 'Рабочий вариант'), ('Разработка', 'Разработка'), ('Проверка', 'Проверка'), ('Проверен', 'Проверен'), ('На согласовании', 'На согласовании'), ('Согласован', 'Согласован'), ('На утверждении', 'На утверждении'), ('Утвержден', 'Утвержден'), ('Отклонен', 'Отклонен'), ('Выпущен', 'Выпущен'), ('Заморожен', 'Заморожен'), ('Заменен', 'Заменен'), ('Заблокирован', 'Заблокирован'), ('Аннулирован', 'Аннулирован'), ('На пересмотре', 'На пересмотре'), ('Архив', 'Архив')], default='Зарегистрирован', max_length=30),
        ),
        migrations.AlterField(
            model_name='generaldrawingunit',
            name='status',
            field=models.CharField(choices=[('Зарегистрирован', 'Зарегистрирован'), ('Рабочий вариант', 'Рабочий вариант'), ('Разработка', 'Разработка'), ('Проверка', 'Проверка'), ('Проверен', 'Проверен'), ('На согласовании', 'На согласовании'), ('Согласован', 'Согласован'), ('На утверждении', 'На утверждении'), ('Утвержден', 'Утвержден'), ('Отклонен', 'Отклонен'), ('Выпущен', 'Выпущен'), ('Заморожен', 'Заморожен'), ('Заменен', 'Заменен'), ('Заблокирован', 'Заблокирован'), ('Аннулирован', 'Аннулирован'), ('На пересмотре', 'На пересмотре'), ('Архив', 'Архив')], default='Зарегистрирован', max_length=30),
        ),
        migrations.AlterField(
            model_name='generalelectricaldiagram',
            name='status',
            field=models.CharField(choices=[('Зарегистрирован', 'Зарегистрирован'), ('Рабочий вариант', 'Рабочий вариант'), ('Разработка', 'Разработка'), ('Проверка', 'Проверка'), ('Проверен', 'Проверен'), ('На согласовании', 'На согласовании'), ('Согласован', 'Согласован'), ('На утверждении', 'На утверждении'), ('Утвержден', 'Утвержден'), ('Отклонен', 'Отклонен'), ('Выпущен', 'Выпущен'), ('Заморожен', 'Заморожен'), ('Заменен', 'Заменен'), ('Заблокирован', 'Заблокирован'), ('Аннулирован', 'Аннулирован'), ('На пересмотре', 'На пересмотре'), ('Архив', 'Архив')], default='Зарегистрирован', max_length=30),
        ),
        migrations.AlterField(
            model_name='reporttechnicalproposal',
            name='status',
            field=models.CharField(choices=[('Зарегистрирован', 'Зарегистрирован'), ('Рабочий вариант', 'Рабочий вариант'), ('Разработка', 'Разработка'), ('Проверка', 'Проверка'), ('Проверен', 'Проверен'), ('На согласовании', 'На согласовании'), ('Согласован', 'Согласован'), ('На утверждении', 'На утверждении'), ('Утвержден', 'Утвержден'), ('Отклонен', 'Отклонен'), ('Выпущен', 'Выпущен'), ('Заморожен', 'Заморожен'), ('Заменен', 'Заменен'), ('Заблокирован', 'Заблокирован'), ('Аннулирован', 'Аннулирован'), ('На пересмотре', 'На пересмотре'), ('Архив', 'Архив')], default='Зарегистрирован', max_length=50),
        ),
        migrations.AlterField(
            model_name='softwareproduct',
            name='status',
            field=models.CharField(choices=[('Зарегистрирован', 'Зарегистрирован'), ('Рабочий вариант', 'Рабочий вариант'), ('Разработка', 'Разработка'), ('Проверка', 'Проверка'), ('Проверен', 'Проверен'), ('На согласовании', 'На согласовании'), ('Согласован', 'Согласован'), ('На утверждении', 'На утверждении'), ('Утвержден', 'Утвержден'), ('Отклонен', 'Отклонен'), ('Выпущен', 'Выпущен'), ('Заморожен', 'Заморожен'), ('Заменен', 'Заменен'), ('Заблокирован', 'Заблокирован'), ('Аннулирован', 'Аннулирован'), ('На пересмотре', 'На пересмотре'), ('Архив', 'Архив')], default='Зарегистрирован', max_length=50),
        ),
    ]
