# Generated by Django 4.1.6 on 2023-05-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_file_alter_diler_calculator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shapesystem',
            name='photo',
            field=models.ImageField(upload_to='shape/img', verbose_name='Фото 303x323'),
        ),
    ]
