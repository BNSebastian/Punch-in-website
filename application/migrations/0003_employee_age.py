# Generated by Django 4.1 on 2022-08-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_employee_first_name_alter_employee_job_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=13),
        ),
    ]
