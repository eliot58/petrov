from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
from .utils.pass_generator import generator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#LOGIN REGISTER LOGOUT
#============================================================================
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user.is_active:
                if 'remember' not in request.POST:
                    request.session.set_expiry(0)
                    request.session.modified = True
                login(request, user)
                return redirect(index)
            else:
                return render(request, 'auth/disable.html')
    else:
        if request.user.is_authenticated:
            return redirect(index)
        login_form = LoginForm()
    return render(request, 'auth/login.html', {'form': login_form})


def signup(request):
    if request.method == 'POST':
        password = generator(8)
        profile_form = SignupForm(request.POST)
        if profile_form.is_valid():
            cd = profile_form.cleaned_data
            new_user = User()
            new_user.username = cd['email']
            new_user.email = cd['email']
            new_user.set_password(password)
            new_user.save()
            Diler.objects.create(user=new_user,fullName=cd['fullName'],email=cd['email'],phone=cd['phone'])
            msg = 'Вы зарегистрировались в петровских окнах' + '\n' + 'Ваш login: ' + request.POST['email'] + '\n' + 'Ваш password: ' + password
            try:
                send_mail('Регистрация в todotodo', msg, settings.EMAIL_HOST_USER, [request.POST['email']], fail_silently=False)
            except:
                new_user.delete()
                return render(request, 'auth/lose.html')
            return render(request, 'auth/success.html')
    else:
        profile_form = SignupForm()

    return render(request, 'auth/signup.html', {'form': profile_form})

def logout_view(request):
    logout(request)
    return redirect(login_view)

@login_required(login_url='/login/')
def index(request):
    return render(request, 'test/home.html', {'bonuses': Bonus.objects.all(), 'news': New.objects.all()[:5]})

@login_required(login_url='/login/')
def cart(request):
    return render(request, 'test/cart.html', {'prices': Price.objects.all()})

@login_required(login_url='/login/')
def news(request):
    return render(request, 'test/new.html', {'news': New.objects.all()})



@login_required(login_url='/login/')
def profile(request):
    if request.method == 'POST':
        diler = request.user.diler
        diler.fullName = request.POST['fullName']
        diler.email = request.POST['email']
        diler.phone = request.POST['phone']
        diler.alert_phone = request.POST['alert_phone']
        diler.address = request.POST['address']
        diler.manager = request.POST['manager']
        diler.calculator = request.POST['calculator']
        diler.save()
        return render(index)
    return render(request, 'test/profile.html')

@login_required(login_url='/login/')
def orders(request):
    return render(request, 'test/profile.html')

@login_required(login_url='/login/')
def store(request):
    items = Store.objects.all().order_by('id')
    paginator = Paginator(items, 6)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'test/store.html', {'items': items})

@login_required(login_url='/login/')
def notifications(request):
    if request.method == 'POST':
        
        return render(index)
    return render(request, 'test/notifications.html')

@login_required(login_url='/login/')
def shapes(request):
    items = Shape.objects.all().order_by('id')
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'test/shape.html', {'items': items, 'range': range(1,11)})




@login_required(login_url='/login/')
def instructions(request):
    return render(request, 'test/instructions.html', {'instructions': Instructions.objects.all()})

@login_required(login_url='/login/')
def learn(request):
    return render(request, 'test/learn.html', {'learns': Learn.objects.all()})

@login_required(login_url='/login/')
def certificate(request):
    return render(request, 'test/certificate.html', {'certificates': Certificate.objects.all()})

@login_required(login_url='/login/')
def videolearn(request): 
    return render(request, 'test/videolearn.html', {'videolearns': Video.objects.all()})