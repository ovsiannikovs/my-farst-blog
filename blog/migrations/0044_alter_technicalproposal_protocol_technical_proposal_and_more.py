# Generated by Django 5.1.8 on 2025-07-07 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_alter_technicalproposal_list_technical_proposal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicalproposal',
            name='protocol_technical_proposal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.protocoltechnicalproposal'),
        ),
        migrations.AlterField(
            model_name='technicalproposal',
            name='report_technical_proposal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.reporttechnicalproposal'),
        ),
    ]
