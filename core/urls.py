from django.urls import path, re_path as url
from .views import *
from django.contrib.auth import views as auth_views
from .forms import *


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login_view'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset_form.html',email_template_name = 'auth/password_reset_email.html', form_class=ResetPassForm), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name = 'password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html',form_class=PassSetForm), name ='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name = 'password_reset_complete'),
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
    path('commands/', news, name='commands'),
    path('shapes/', shapes, name='shapes'),
    path('cart/', cart, name='cart'),
    path('offers/', offers, name='offers'),
    path('bonus/', bonus, name='bonus'),
    path('ads/', ads, name='ads'),
    path('talon/', talon, name='talon'),
]
