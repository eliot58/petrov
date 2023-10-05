from django.urls import path
from .views import *
from .forms import *


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_core_view'),
    path('price/', price, name='price'),
    path('profile/', profile, name='profile'),
    path('orders/', orders, name='orders'),
    path('store/', store, name='store'),
    path('notifications/', notifications, name='notifications'),
    path('instructions/', instructions, name='instructions'),
    path('learn/', learn, name='learn'),
    path('certificate/', certificate, name='certificate'),
    path('video/', videolearn, name='video'),
    path('commands/', commands, name='commands'),
    path('shapes/', shapes, name='shapes'),
    path('cart/', cart, name='cart'),
    path('offers/', offers, name='offers'),
    path('services/', services, name='services'),
    path('talon/', talon, name='talon'),
    path('cart_item_delete/<int:id>/', cart_item_delete, name="cart_item_delete"),
    path('sample/', sample, name="sample"),
    path('wait/', notwork, name="wait"),
    path('ads-create/<str:order_name>', ads_create, name='ads-create'),
    path('minus/<int:id>/', cart_item_minus),
    path('plus/<int:id>/', cart_item_plus),
    path('clear-cart/', clear_cart, name='clear_cart'),
    path('buy/', buy, name='buy'),
]
