from django.db import models
from django.contrib.auth.models import User

class Diler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Дилер')
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    alert_phone = models.CharField(max_length=12, default='')
    address = models.CharField(max_length=200, default='')
    discount_window = models.IntegerField(default=0)
    accessories_discount = models.IntegerField(default=0)
    manager = models.CharField(max_length=100, default='')
    calculator = models.CharField(max_length=100, default='')
    last_login = models.DateTimeField(auto_now=True)
    last_week_bonus = models.FloatField(default=0)
    bonus = models.FloatField(default=0)

    sms_alert = models.BooleanField(default=False)
    telegram_alert = models.BooleanField(default=False)
    email_alert = models.BooleanField(default=False)

    change_mail = models.BooleanField(default=False)
    change_email = models.BooleanField(default=False)
    change_manager = models.BooleanField(default=False)


    ads_client = models.BooleanField(default=False)
    ads_me = models.BooleanField(default=False)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилеры'


class Order(models.Model):

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'




class Store(models.Model):
    photo = models.FileField(upload_to='store/img')
    title = models.CharField(max_length=20)
    description = models.TextField()
    count = models.IntegerField()
    price_of_bonus = models.IntegerField()
    price  = models.IntegerField()


    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазин'





class Shape(models.Model):
    photo =  models.FileField(upload_to='shape/img')
    name = models.CharField(max_length=40)
    rate = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        
    ]
    warm_proofing = models.IntegerField(choices=rate)
    sound_proofing = models.IntegerField(choices=rate)
    camera = models.IntegerField()
    shape_width = models.CharField(max_length=10)
    shape_height = models.CharField(max_length=10)
    width_glaze = models.CharField(max_length=10)

    warm_proofing_dc = models.CharField(max_length=10)
    sound_proofing_dc = models.CharField(max_length=10)


    class Meta:
        verbose_name = 'Профильная система'
        verbose_name_plural = 'Профильные системы'


class Implement(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
    generator = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Фурнитура'
        verbose_name_plural = 'Фурнитуры'



class Glazing(models.Model):
    articul =  models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    percent = models.FloatField()
    


    class Meta:
        verbose_name = 'Стеклопакет'
        verbose_name_plural = 'Стеклопакеты'




class Bonus(models.Model):
    item = models.ForeignKey(Store, on_delete=models.CASCADE)
    unit = models.PositiveIntegerField()
    count = models.FloatField()

    class Meta:
        verbose_name = 'Бонус'
        verbose_name_plural = 'Бонусы'



class Price(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Логистика'
        verbose_name_plural = 'Логистика'

class Role(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

class Employ(models.Model):
    fullName = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    photo = models.FileField(upload_to='employ')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class New(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новинка'
        verbose_name_plural = 'Новинки'


class Instructions(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='learn/instructions')

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'


class Learn(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='learn/materials')


    class Meta:
        verbose_name = 'Учебные материал'
        verbose_name_plural = 'Учебные материалы'



class Certificate(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='certificate')


    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Video(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='learn/video')


    class Meta:
        verbose_name = 'Видео обучение'
        verbose_name_plural = 'Видео обучение'



