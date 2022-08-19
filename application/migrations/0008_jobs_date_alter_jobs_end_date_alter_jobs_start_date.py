# Generated by Django 4.1 on 2022-08-11 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_alter_jobs_description_alter_jobs_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date:'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='end_date',
            field=models.TimeField(default=datetime.date.today, verbose_name='Ended at:'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='start_date',
            field=models.TimeField(default=datetime.date.today, verbose_name='Started at:'),
        ),
    ]
