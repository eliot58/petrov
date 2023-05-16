import json
from django.db import models
from django.contrib.auth.models import User


with open("shape.json", "r") as f:
    data = json.load(f)
shapes = [(shape["name"], shape["name"]) for shape in data]


with open("implement.json", "r") as f:
    data = json.load(f)
implements = [(implement["name"], implement["name"]) for implement in data]


with open("glazing.json", "r") as f:
    data = json.load(f)
glazings = [(glazing["marking"], glazing["marking"]) for glazing in data]


class Store(models.Model):
    photo = models.FileField(upload_to='store/img', verbose_name='Фото 303x323')
    title = models.CharField(max_length=20, unique=True, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    count = models.IntegerField(verbose_name='В наличии')
    price_of_bonus = models.PositiveIntegerField(verbose_name='Цена в бонусах')
    price  = models.PositiveIntegerField(verbose_name='Цена в рублях')

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазин'


class Region(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name='Регион')


    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
    


    


class Diler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Дилер')
    fullName = models.CharField(max_length=100, verbose_name='Название компании')
    email = models.EmailField(verbose_name='E-mail', blank=True)
    phone = models.CharField(max_length=12, verbose_name='Телефон', blank=True)
    alert_phone = models.CharField(max_length=12, default='', verbose_name='Телефон для уведомлений')
    address = models.CharField(max_length=200, default='', verbose_name='Адрес')
    discount_window = models.IntegerField(default=0, verbose_name='Скидка на окна')
    accessories_discount = models.IntegerField(default=0, verbose_name='Скидка на аксессуары')
    manager = models.CharField(max_length=100, default='', verbose_name='Территориальный менеджер')
    calculator = models.CharField(max_length=100, default='', verbose_name='Расчетчик')
    last_login = models.DateTimeField(verbose_name='Дата последнего входа')
    seller_code = models.CharField(max_length=20, unique=True)

    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Регион')

    sms_alert = models.BooleanField(default=False, verbose_name='SMS')
    telegram_alert = models.BooleanField(default=False, verbose_name='Telegram')
    email_alert = models.BooleanField(default=False, verbose_name='E-mail')

    change_mail = models.BooleanField(default=False, verbose_name='Отправка по почте')
    change_email = models.BooleanField(default=False, verbose_name='Отправка по e-mail')
    change_manager = models.BooleanField(default=False, verbose_name='Менеджером в руки')


    ads_client = models.BooleanField(default=False, verbose_name='Решение с клиентом')
    ads_me = models.BooleanField(default=False, verbose_name='Решение через меня')

    cart = models.JSONField(default=dict())

    total_price = models.PositiveIntegerField(default=0)

    def count(self):
        return len(self.cart.items())

    

    def __str__(self):
        return self.fullName


    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилеры'


class DilerBonus(models.Model):
    seller_code = models.CharField(max_length=20, unique=True)
    total_bonus = models.PositiveIntegerField(default=0)



class ShapeSystem(models.Model):
    photo =  models.FileField(upload_to='shape/img', verbose_name='Фото 303x323')
    name = models.CharField(max_length=300, choices=shapes)
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
    warm_proofing = models.IntegerField(choices=rate, verbose_name='Теплоизоляция')
    sound_proofing = models.IntegerField(choices=rate, verbose_name='Шумоизоляция')
    camera = models.IntegerField(verbose_name='Количество камер')
    shape_width = models.CharField(max_length=10, verbose_name='Ширина профиля')
    shape_height = models.CharField(max_length=10, verbose_name='Высота рамы')
    width_glaze = models.CharField(max_length=10, verbose_name='Ширина стеклопакета')

    warm_proofing_dc = models.CharField(max_length=10, verbose_name='Сопротивление теплопередачи в Дц')
    sound_proofing_dc = models.CharField(max_length=10, verbose_name='Шумоизоляция в Дц')



    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'Профильная система'
        verbose_name_plural = 'Профильные системы'





class Bonus(models.Model):
    fr = models.DateField(verbose_name='Период от')
    to = models.DateField(verbose_name='Период до')
    ch = [
        ('s', 'Профиль'),
        ('i', 'Фурнитура'),
        ('g', 'Стеклопакет')
    ]
    select = models.CharField(max_length=10, choices=ch)

    shape = models.CharField(choices=shapes, max_length=300, blank=True, null=True, verbose_name='Профильная система')
    implement = models.CharField(choices=implements, max_length=300, blank=True, null=True, verbose_name='Фурнитура')
    glazing = models.CharField(choices=glazings, max_length=300, blank=True, null=True, verbose_name='Стеклопакет')

    u = [
        ('m2', 'm2'),
        ('шт', 'шт')
    ]
    
    unit = models.CharField(max_length=5,choices=u, verbose_name='Единица измерения')
    count = models.FloatField(verbose_name='Бонусы')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'



class Price(models.Model):
    zone = models.PositiveIntegerField(unique=True)
    region = models.OneToOneField(Region, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Логистика'
        verbose_name_plural = 'Логистика'

class Role(models.Model):
    name = models.CharField(max_length=80, verbose_name='Роль')


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

class Employ(models.Model):
    fullName = models.CharField(max_length=100, verbose_name='ФИО')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Роль')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.EmailField(verbose_name='E-mail')
    photo = models.FileField(upload_to='employ', verbose_name='Фото 303x323')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class New(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    file = models.FileField(upload_to='news', verbose_name='Файл')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Instructions(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    file = models.FileField(upload_to='learn/instructions', verbose_name='Файл')

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'


class Learn(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    file = models.FileField(upload_to='learn/materials', verbose_name='Файл')


    class Meta:
        verbose_name = 'Учебные материал'
        verbose_name_plural = 'Учебные материалы'



class Certificate(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    file = models.FileField(upload_to='certificate', verbose_name='Файл')


    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    file = models.FileField(upload_to='learn/video', verbose_name='Файл')


    class Meta:
        verbose_name = 'Видео обучение'
        verbose_name_plural = 'Видео обучение'



class Offers(models.Model):
    shape = models.CharField(choices=shapes, max_length=300, verbose_name='Профиль')
    implement = models.CharField(choices=implements, max_length=300, verbose_name='Фурнитура')
    glazing = models.CharField(choices=glazings, max_length=300, verbose_name='Стеклопакет')
    size = models.CharField(max_length=20, verbose_name='Размер')
    price = models.PositiveIntegerField(verbose_name='Базовая цена')

    class Meta:
        verbose_name = 'Коммерческое предложение'
        verbose_name_plural = 'Коммерческие предложения'


class Sample(models.Model):
    file = models.FileField(upload_to="sample")

    def __str__(self) -> str:
        return "Акт замеров"
    

    def save(self, *args, **kwargs):
        if len(Sample.objects.all()) != 0:
            return
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Акт замеров'
        verbose_name_plural = 'Акт замеров'

class File(models.Model):
    file = models.FileField(upload_to="service")

    def __str__(self) -> str:
        return self.id
    
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'