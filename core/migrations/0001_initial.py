# Generated by Django 4.1.5 on 2023-02-07 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификаты',
            },
        ),
        migrations.CreateModel(
            name='Glazing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articul', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=40)),
                ('percent', models.FloatField()),
            ],
            options={
                'verbose_name': 'Стеклопакет',
                'verbose_name_plural': 'Стеклопакеты',
            },
        ),
        migrations.CreateModel(
            name='Implement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=30)),
                ('generator', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Фурнитура',
                'verbose_name_plural': 'Фурнитуры',
            },
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Инструкция',
                'verbose_name_plural': 'Инструкции',
            },
        ),
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Учебные материал',
                'verbose_name_plural': 'Учебные материалы',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Новинка',
                'verbose_name_plural': 'Новинки',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Логистика',
                'verbose_name_plural': 'Логистика',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=40)),
                ('warm_proofing', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('sound_proofing', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('camera', models.IntegerField()),
                ('shape_width', models.CharField(max_length=10)),
                ('shape_height', models.CharField(max_length=10)),
                ('width_glaze', models.CharField(max_length=10)),
                ('warm_proofing_dc', models.CharField(max_length=10)),
                ('sound_proofing_dc', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Профильная система',
                'verbose_name_plural': 'Профильные системы',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('count', models.IntegerField()),
                ('price_of_bonus', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазин',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Видео обучение',
                'verbose_name_plural': 'Видео обучение',
            },
        ),
        migrations.CreateModel(
            name='Employ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.FileField(upload_to='')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.role')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Diler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('alert_phone', models.CharField(default='', max_length=12)),
                ('address', models.CharField(default='', max_length=200)),
                ('discount_window', models.IntegerField(default=0)),
                ('accessories_discount', models.IntegerField(default=0)),
                ('manager', models.CharField(default='', max_length=100)),
                ('calculator', models.CharField(default='', max_length=100)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('last_week_bonus', models.FloatField(default=0)),
                ('bonus', models.FloatField(default=0)),
                ('sms_alert', models.BooleanField(default=False)),
                ('telegram_alert', models.BooleanField(default=False)),
                ('email_alert', models.BooleanField(default=False)),
                ('change_mail', models.BooleanField(default=False)),
                ('change_email', models.BooleanField(default=False)),
                ('change_manager', models.BooleanField(default=False)),
                ('ads_client', models.BooleanField(default=False)),
                ('ads_me', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Дилер')),
            ],
            options={
                'verbose_name': 'Дилер',
                'verbose_name_plural': 'Дилеры',
            },
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.PositiveIntegerField()),
                ('count', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.store')),
            ],
            options={
                'verbose_name': 'Бонус',
                'verbose_name_plural': 'Бонусы',
            },
        ),
    ]
