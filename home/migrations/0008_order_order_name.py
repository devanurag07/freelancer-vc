# Generated by Django 3.2.3 on 2021-07-18 15:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_order_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_name',
            field=models.CharField(default=datetime.datetime(2021, 7, 18, 15, 42, 15, 440965, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
    ]
