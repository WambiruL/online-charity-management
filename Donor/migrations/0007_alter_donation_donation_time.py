# Generated by Django 3.2.6 on 2021-08-05 10:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0006_auto_20210805_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 10, 23, 36, 522573, tzinfo=utc)),
        ),
    ]
