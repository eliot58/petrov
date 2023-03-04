from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Store(models.Model):
    photo = models.FileField(upload_to='store/img', verbose_name='Фото')
    title = models.CharField(max_length=20,unique=True, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    count = models.IntegerField(verbose_name='В наличии')
    price_of_bonus = models.PositiveIntegerField(verbose_name='Цена в бонусах')
    price  = models.PositiveIntegerField(verbose_name='Цена в рублях')

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазин'
    


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
    bonus = models.FloatField(default=0, verbose_name='Бонусы дилера')
    seller_code = models.CharField(max_length=20)

    sms_alert = models.BooleanField(default=False, verbose_name='E-mail')
    telegram_alert = models.BooleanField(default=False, verbose_name='SMS')
    email_alert = models.BooleanField(default=False, verbose_name='Telegram')

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
        return self.name


    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилеры'





class Shape(models.Model):
    photo =  models.FileField(upload_to='shape/img', verbose_name='Фото')
    name = models.CharField(max_length=40,unique=True, verbose_name='Название')
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


class Implement(models.Model):
    name = models.CharField(max_length=40,unique=True, verbose_name='Название')

    country = CountryField(verbose_name='Страна производителя')
    generator = models.CharField(max_length=30, verbose_name='Производитель')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Фурнитура'
        verbose_name_plural = 'Фурнитуры'



class Glazing(models.Model):
    articul =  models.CharField(max_length=20,unique=True, verbose_name='Артикул')
    name = models.CharField(max_length=40, verbose_name='Название')
    percent = models.FloatField(verbose_name='Процент')

    def __str__(self) -> str:
        return self.name
    


    class Meta:
        verbose_name = 'Стеклопакет'
        verbose_name_plural = 'Стеклопакеты'

class Unit(models.Model):
    unit = models.CharField(max_length=10)


    def __str__(self) -> str:
        return self.unit

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


class Bonus(models.Model):
    item = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='Товар')
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE,verbose_name='Единица измерения')
    count = models.FloatField(verbose_name='Бонусы')

    class Meta:
        verbose_name = 'Бонус'
        verbose_name_plural = 'Бонусы'



class Price(models.Model):
    zone = models.PositiveIntegerField()
    region = models.CharField(max_length=40,unique=True, verbose_name='Регион')
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
    photo = models.FileField(upload_to='employ', verbose_name='Фото')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class New(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

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
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, verbose_name='Профиль')
    implement = models.ForeignKey(Implement, on_delete=models.CASCADE, verbose_name='Фурнитура')
    glazing = models.ForeignKey(Glazing, on_delete=models.CASCADE, verbose_name='Стеклопакет')
    size = models.CharField(max_length=20, verbose_name='Размер')
    price = models.PositiveIntegerField(verbose_name='Базовая цена')

    class Meta:
        verbose_name = 'Коммерческое предложение'
        verbose_name_plural = 'Коммерческие предложения'


class Sample(models.Model):
    file = models.FileField(upload_to="sample")

    class Meta:
        verbose_name = 'Акт замеров'
        verbose_name_plural = 'Акт замеров'
