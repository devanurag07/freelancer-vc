# Generated by Django 2.1.15 on 2021-12-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20211122_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='costumer_price',
            field=models.CharField(default='Not defined Yet', max_length=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='laundry_price',
            field=models.CharField(default='Not defined Yet', max_length=1000),
        ),
    ]