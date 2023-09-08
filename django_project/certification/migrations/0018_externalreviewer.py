# Generated by Django 3.2.13 on 2022-04-20 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0017_auto_20220419_0519'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalReviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=100)),
                ('email', models.EmailField(help_text='Email address of the reviewer', max_length=254)),
                ('certifying_organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='certification.certifyingorganisation')),
            ],
        ),
    ]