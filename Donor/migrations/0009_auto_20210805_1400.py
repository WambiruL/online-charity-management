# Generated by Django 3.2.6 on 2021-08-05 11:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Donor', '0008_auto_20210805_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 11, 0, 0, 829115, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Donor.donation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
