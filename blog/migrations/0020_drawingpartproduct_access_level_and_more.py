# Generated by Django 5.1.8 on 2025-06-02 11:39

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_electronicmodelpartunit_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='drawingpartproduct',
            name='access_level',
            field=models.CharField(choices=[('О', 'Общий'), ('К', 'Конфиденциально'), ('С', 'Секретно'), ('СС', 'Совершенно секретно')], default='О', max_length=10),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='access_rights',
            field=models.CharField(default='7', max_length=50),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='application',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='approval_cycle',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drawing_part_product_authors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='category',
            field=models.CharField(choices=[('ЧД ВО', 'Чертеж детали изделия')], default='ЧД ВО', max_length=50),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='change_number',
            field=models.CharField(default='Изм. 1', max_length=20),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='current_responsible',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drawing_part_product_responsibles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='date_of_change',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='date_of_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='desig_document',
            field=models.CharField(default=1, max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='develop_org',
            field=models.CharField(default='ООО "СИСТЕМА"', max_length=100),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='file',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='info_format',
            field=models.CharField(choices=[('ДЭ', 'ДЭ'), ('ДЭ КД', 'ДЭ КД'), ('ТДЭ', 'ТДЭ'), ('ДБ КД', 'ДБ КД')], default='ДЭ', max_length=10),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='language',
            field=models.CharField(default='rus', max_length=10),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='last_editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drawing_part_product_editors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='litera',
            field=models.CharField(default='П-', max_length=20),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='pattern',
            field=models.CharField(blank=True, default='ЧД ВО ПТ', max_length=50),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='primary_use',
            field=models.CharField(default='СИ.40522001.000.13ВПТ', max_length=100),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='priority',
            field=models.CharField(blank=True, choices=[('Срочно', 'Срочно'), ('Высокий', 'Высокий'), ('Средний', 'Средний'), ('Низкий', 'Низкий')], max_length=30),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='status',
            field=models.CharField(choices=[('Рабочий вариант', 'Рабочий вариант'), ('На согласовании', 'На согласовании')], default='Рабочий вариант', max_length=50),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='subscribers',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='trl',
            field=models.CharField(choices=[('1-', '1-'), ('2-', '2-'), ('2', '2'), ('3-', '3-'), ('3', '3')], default='1-', max_length=10),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='validity_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='version',
            field=models.CharField(default='v1.0', max_length=6),
        ),
        migrations.AddField(
            model_name='drawingpartproduct',
            name='version_diff',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='drawingpartproduct',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
