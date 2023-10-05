import re
from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Diler
from django.core.exceptions import ValidationError
import requests
import json
from django.utils import timezone

class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder": "Логин"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), label='')

    def clean_password(self):
        password = self.cleaned_data['password']
        username = self.cleaned_data['username']

        epassword = password.replace("+", "%252B")
        eusername = username.replace("+", "%252B")

        r = requests.get(f'http://176.62.187.250/auth.php?jsoncallback=jQuery1113007469605505475574_1676738570680&login={eusername}&passwd={epassword}')
        s = r.text
        start = s.index('(')
        end = s.rindex(')')
        json_string = s[start+1:end]

        data = json.loads(json_string)

        if data['seller_code'] == 'empty' or data['seller_name'] == 'empty':
            raise ValidationError('Неверный email или пароль')
        else:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                new_user = User()
                new_user.username = username
                new_user.set_password(password)
                new_user.save()
                Diler.objects.create(user=new_user,fullName=data['seller_name'], seller_code=data['seller_code'], last_login=timezone.now())
                return password
            else:
                return password
        
        # try:
        #     user = User.objects.get(username=username)
        # except User.DoesNotExist:
        #     raise ValidationError('Неверный email или пароль')
        # else:
        #     if not(check_password(password, user.password)):
        #         raise ValidationError('Неверный email или пароль')
        # return password
                
        
class OrderNameForm(forms.Form):
    order_name = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder": "Введите номер заказа в формате", "style": "background-color: inherit;"}))

    def clean_order_name(self):
        order_name = self.cleaned_data["order_name"]

        s_code = self.data["s_code"]

        t = 1 if order_name.strip().split("\\")[0] == 'О' else 2
        order_id = order_name.strip().split('\\')[1]
        r = requests.get(f'http://176.62.187.250/isorder.php?order_id={order_id}&type={t}')
        data = json.loads(r.text)

        if len(data) == 0:
            raise ValidationError('Такого заказа не существует')
        else:
            if data[0]["seller_code"] != s_code:
                raise ValidationError('Это не ваш заказ')
        
        return order_name