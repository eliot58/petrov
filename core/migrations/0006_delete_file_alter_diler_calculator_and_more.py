# Generated by Django 4.1.6 on 2023-05-19 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_dilerbonus_file_remove_diler_bonus_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
        migrations.AlterField(
            model_name='diler',
            name='calculator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calculator', to='core.employ', verbose_name='Расчетчик'),
        ),
        migrations.AlterField(
            model_name='diler',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager', to='core.employ', verbose_name='Территориальный менеджер'),
        ),
        migrations.AlterField(
            model_name='new',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='news', verbose_name='Файл'),
        ),
    ]