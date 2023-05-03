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
    path('news/', news, name='news'),
    path('commands/', commands, name='commands'),
    path('shapes/', shapes, name='shapes'),
    path('cart/', cart, name='cart'),
    path('offers/', offers, name='offers'),
    path('bonus/', bonus, name='bonus'),
    path('ads/', ads, name='ads'),
    path('talon/', talon, name='talon'),
    path('cart_item_delete/<int:id>/', cart_item_delete, name="cart_item_delete"),
    path('sample/', sample, name="sample"),
    path('wait/', notwork, name="wait"),
    path('ads-id/', ads_id, name='ads-id'),
    path('ads-create/', ads_create, name='ads-create'),
]
