# Generated by Django 5.1.7 on 2025-03-25 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=1800)),
        ),
    ]
