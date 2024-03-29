# Generated by Django 4.1.6 on 2023-05-31 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_calculatemanager_territorymanager_alter_employ_role_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculatemanager',
            name='name',
        ),
        migrations.RemoveField(
            model_name='territorymanager',
            name='name',
        ),
        migrations.AddField(
            model_name='calculatemanager',
            name='description',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calculatemanager',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calculatemanager',
            name='fullName',
            field=models.CharField(default='', max_length=80, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calculatemanager',
            name='phone',
            field=models.CharField(default='', max_length=12, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calculatemanager',
            name='photo',
            field=models.ImageField(default='', upload_to='employ', verbose_name='Фото 200x200'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employ',
            name='description',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='territorymanager',
            name='description',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='territorymanager',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='territorymanager',
            name='fullName',
            field=models.CharField(default='', max_length=80, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='territorymanager',
            name='phone',
            field=models.CharField(default='', max_length=12, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='territorymanager',
            name='photo',
            field=models.ImageField(default='', upload_to='employ', verbose_name='Фото 200x200'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employ',
            name='fullName',
            field=models.CharField(max_length=80, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='photo',
            field=models.ImageField(upload_to='employ', verbose_name='Фото 200x200'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='role',
            field=models.CharField(choices=[('director', 'Собственник'), ('development', 'Руководитель отдела развития'), ('service', 'Менеджер по рекламациям')], max_length=60),
        ),
    ]
