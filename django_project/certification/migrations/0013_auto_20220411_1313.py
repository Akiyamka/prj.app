# Generated by Django 2.2.18 on 2022-04-11 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0012_auto_20220323_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='target',
            field=models.CharField(blank=True, choices=[('organization_owner', 'Organization Owner'), ('reviewer', 'Reviewer')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='historicalchecklist',
            name='target',
            field=models.CharField(blank=True, choices=[('organization_owner', 'Organization Owner'), ('reviewer', 'Reviewer')], default='', max_length=100),
        ),
    ]