# Generated by Django 3.2.3 on 2021-09-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_services_s_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='f_stat',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
