# Generated by Django 4.1.6 on 2023-05-31 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_calculatemanager_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='photo',
            field=models.ImageField(default='', upload_to='employ', verbose_name='Фото 200x200'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='territorymanager',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='territorymanager',
            name='photo',
            field=models.ImageField(default='', upload_to='employ', verbose_name='Фото 200x200'),
            preserve_default=False,
        ),
    ]
