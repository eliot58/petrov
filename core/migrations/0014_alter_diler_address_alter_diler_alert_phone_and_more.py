# Generated by Django 4.1.6 on 2023-05-31 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_employ_phone_alter_employ_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diler',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='diler',
            name='alert_phone',
            field=models.CharField(blank=True, default='', max_length=12, verbose_name='Телефон для уведомлений'),
        ),
        migrations.AlterField(
            model_name='diler',
            name='cart',
            field=models.JSONField(blank=True, default={}),
        ),
    ]
