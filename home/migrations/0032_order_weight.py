# Generated by Django 2.1.15 on 2021-10-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_deleted_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='weight',
            field=models.CharField(default='Not specified', max_length=1000),
            preserve_default=False,
        ),
    ]
