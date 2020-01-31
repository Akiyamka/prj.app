# Generated by Django 2.2 on 2020-01-10 05:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_project_credit_cost_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sponsorship_managers',
            field=models.ManyToManyField(blank=True, help_text='Managers of the sponsorship in this project. They will be allowed to approve sustaining member entries in the moderation queue.', related_name='sponsorship_managers', to=settings.AUTH_USER_MODEL, verbose_name='Sustaining member managers'),
        ),
    ]