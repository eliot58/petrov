# Generated by Django 4.1.6 on 2023-03-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_bonus_fr_alter_bonus_glazing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='unit',
            field=models.CharField(choices=[('m2', 'm2'), ('st', 'шт')], max_length=5, verbose_name='Единица измерения'),
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
