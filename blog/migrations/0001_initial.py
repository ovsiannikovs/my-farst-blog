# Generated by Django 5.1.8 on 2025-05-05 13:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('desig_product', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('date_of_change', models.DateTimeField(auto_now=True)),
                ('version', models.CharField(max_length=20)),
                ('version_diff', models.TextField(blank=True, max_length=1000)),
                ('litera', models.CharField(max_length=20)),
                ('trl', models.CharField(max_length=10)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_products', to=settings.AUTH_USER_MODEL)),
                ('current_responsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsible_products', to=settings.AUTH_USER_MODEL)),
                ('last_editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edited_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
