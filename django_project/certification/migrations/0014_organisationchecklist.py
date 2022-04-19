# Generated by Django 2.2.18 on 2022-04-12 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certification', '0013_auto_20220411_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationChecklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklist_target', models.CharField(blank=True, choices=[('organization_owner', 'Organization Owner'), ('reviewer', 'Reviewer')], default='', max_length=100)),
                ('checklist_question', models.TextField(help_text='Original question from checklist.')),
                ('checked', models.BooleanField(default=False, help_text='Indicate whether the checklist is checked or not.')),
                ('text_box_content', models.TextField(blank=True, help_text='Content in text box if available.', null=True)),
                ('checklist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='certification.Checklist')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certification.CertifyingOrganisation')),
                ('submitter', models.ForeignKey(blank=True, help_text='User who submitted the checklist.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checklist_submitter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]