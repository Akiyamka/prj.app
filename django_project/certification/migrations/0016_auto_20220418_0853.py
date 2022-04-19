# Generated by Django 3.2.13 on 2022-04-18 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0015_organisationchecklist_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(default=datetime.date.today, help_text='Course end date', verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(default=datetime.date.today, help_text='Course start date', verbose_name='Start date'),
        ),
    ]