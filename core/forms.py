import re
from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Diler
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
import requests
import json
from django.utils import timezone

class SignupForm(forms.Form):
    fullName = forms.CharField(max_length=100,label='',widget=forms.TextInput(attrs={"placeholder": "Введите ФИО"}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={"placeholder": "Введите почту"}))
    phone = forms.CharField(max_length=12,label='',widget=forms.TextInput(attrs={"placeholder": "Введите номер телефона"}))


    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(username=email)
        except User.DoesNotExist:
            pass
        else:
            raise ValidationError('Пользователь с такой почтой уже есть')
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        regx = re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',phone)
        try:
            regx.start()
        except AttributeError:
            raise ValidationError('Введите правильный номер (+79855310868)')
        try:
            Diler.objects.get(phone=phone)
        except Diler.DoesNotExist:
            pass
        else:
            raise ValidationError('Пользователь с таким номером уже есть')
        return phone

class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder": "E-mail"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), label='')

    def clean_password(self):
        password = self.cleaned_data['password']
        username = self.cleaned_data['username']

        r = requests.get(f'http://176.62.187.250/auth.php?jsoncallback=jQuery1113007469605505475574_1676738570680&login={username}&passwd={password}')
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
                new_user.email = username
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
                
        

class ResetPassForm(PasswordResetForm):
    email = forms.EmailField(
        label='',
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "placeholder": "email"}),
    )

class PassSetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "новый пароль"}),
        strip=False
    )
    new_password2 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "подтверждение пароля"}),
    )


    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    'пароли не совпадают'
                )
        return password2
