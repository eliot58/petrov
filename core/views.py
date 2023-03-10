from pathlib import Path
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import json
from django.utils import timezone
from datetime import datetime
from python_docx_replace import docx_replace
from docx import Document
import os
from django.core.files import File
    



#LOGIN LOGOUT
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


def logout_view(request):
    logout(request)
    return redirect(login_view)



@login_required(login_url='/login/')
def index(request):
    diler = request.user.diler
    diler.last_login = timezone.now()
    diler.save()

    return render(request, 'cabinet/main.html', {'bonuses': Bonus.objects.all()[:3], 'news': New.objects.all()[:5]})

@login_required(login_url='/login/')
def ads(request):
    return render(request, 'cabinet/price.html', {'prices': Price.objects.all()})

@login_required(login_url='/login/')
def talon(request):
    if request.method == "POST":
        f = []
        r = requests.get(f"http://176.62.187.250/loadpic.php?order_id={request.POST['order_id']}")
        items = json.loads(r.text)
        for i in range(len(items)):
            doc = Document("passport.docx")

            my_dict = {
                "o_name": items[i]['o_name'],
                "qu": items[i]['qu'],
                "p_name": items[i]['p_name'],
                "f_name": items[i]['f_name'],
                "c1_name": items[i]['c1_name'],
                "c2_name": items[i]['c2_name'],
                "sqr": items[i]['sqr'],
                "numpos": items[i]['numpos'],
                "glasses": items[i]['glasses'],
            }

            docx_replace(doc, **my_dict)
            
            doc.save(f"render/replace{i}.docx")

            f.append(f"render/replace{i}.docx")
            docs = []
            i = 0
            for item in f:
                docs.append(Document(item))
                if (i != 0):
                    docs[i].add_page_break()
                    for element in docs[i].element.body:
                        docs[0].element.body.append(element)
                i = i + 1
            docs[0].save('render.docx')

        passport = Passports()
        passport.diler = request.user.diler
        path = Path('render.docx')
        with path.open(mode='rb') as f:
            passport.file = File(f,name=path.name)
            passport.save()

        return redirect(passport.file.url)
        

    return render(request, 'cabinet/talon.html')

def price(request):
    return render(request, 'cabinet/price.html', {'prices': Price.objects.all().order_by('zone')})

@login_required(login_url='/login/')
def cart(request):
    if request.method == 'POST':
        diler = request.user.diler
        item = Store.objects.get(id=request.POST["item_id"])
        if str(item.id) in diler.cart:
            diler.cart[str(item.id)]['count'] += int(request.POST['count'])
            diler.cart[str(item.id)]['all_price'] += int(item.price) * int(request.POST['count'])
        else:
            diler.cart[item.id] = {
                'photo': item.photo.url,
                'title': item.title,
                'price': item.price,
                'price_of_bonus': item.price_of_bonus,
                'count': int(request.POST["count"]),
                'all_price': int(item.price) * int(request.POST['count'])
            }
        for key, value in diler.cart.items():
            diler.total_price += int(value['all_price'])
        diler.save()
        return redirect(store)
    print(request.user.diler.cart)
    return render(request, 'cabinet/cart.html', {'items': request.user.diler.cart.items()})

@login_required(login_url='/login/')
def cart_item_delete(request, id):
    diler = request.user.diler
    del diler.cart[str(id)]
    diler.save()
    return redirect(cart)


def news(request):
    return render(request, 'cabinet/news.html', {'news': New.objects.all()})

def bonus(request):
    return render(request, 'cabinet/bonus.html', {'bonuses': Bonus.objects.all()})


def offers(request):
    return render(request, 'cabinet/offers.html', {'offers': Offers.objects.all()})


def sample(request):
    return redirect(Sample.objects.get(id=1).file.url)


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
        return redirect(profile)
    return render(request, 'cabinet/profile.html')

@login_required(login_url='/login/')
def orders(request):
    if 'create_date_to' in request.GET:
        r = requests.get(f'http://176.62.187.250/loadDataForGridPerSellerCode.php?jsoncallback=jQuery1113010583719635799582_1676741279402&s_code={request.user.diler.seller_code}&create_date_from={request.GET["create_date_from"]}-01-01&create_date_to={request.GET["create_date_to"]}&order_id_from=&order_id_to=&manufacture_date_from=&manufacture_date_to=&ready_date_from=&ready_date_to=&filter_select_state=')
    else:
        current_datetime = datetime.now()
        r = requests.get(f'http://176.62.187.250/loadDataForGridPerSellerCode.php?jsoncallback=jQuery1113010583719635799582_1676741279402&s_code={request.user.diler.seller_code}&create_date_from={current_datetime.year}-01-01&create_date_to={current_datetime.date()}&order_id_from=&order_id_to=&manufacture_date_from=&manufacture_date_to=&ready_date_from=&ready_date_to=&filter_select_state=')
    s = r.text
    start = s.index('(')
    end = s.rindex(')')
    json_string = s[start+1:end]



    items = json.loads(json_string)

    if 'search' in request.GET:
        newitems = []
        for item in items:
            if item['order_name'].find(request.GET['search']) != -1:
                newitems.append(item)
                continue
            if item['prof_name'].find(request.GET['search']) != -1:
                newitems.append(item)
                continue
            if item['furn_name'].find(request.GET['search']) != -1:
                newitems.append(item)
                continue
            if item['sp_name'].find(request.GET['search']) != -1:
                newitems.append(item)

        items = newitems

    paginator = Paginator(items, int(request.GET['table_length']) if 'table_length' in request.GET else 5)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)


    return render(request, 'cabinet/orders.html', {'items': items})

@login_required(login_url='/login/')
def store(request):
    items = Store.objects.all().order_by('id')
    paginator = Paginator(items, 4)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'cabinet/store.html', {'items': items})

@login_required(login_url='/login/')
def notifications(request):
    if request.method == 'POST':
        diler = request.user.diler
        diler.sms_alert = True if 'sms_alert' in request.POST else False
        diler.telegram_alert = True if 'telegram_alert' in request.POST else False
        diler.email_alert = True if 'email_alert' in request.POST else False
        diler.change_mail = True if 'change_mail' in request.POST else False
        diler.change_email = True if 'change_email' in request.POST else False
        diler.change_manager = True if 'change_manager' in request.POST else False
        diler.ads_client = True if 'ads_client' in request.POST else False
        diler.ads_me = True if 'ads_me' in request.POST else False
        diler.save()
        return redirect(notifications)
    return render(request, 'cabinet/notifications.html')

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
    return render(request, 'cabinet/shapes.html', {'items': items, 'range': range(1,11)})

def instructions(request):
    return render(request, 'cabinet/instructions.html', {'instructions': Instructions.objects.all()})

def learn(request):
    return render(request, 'cabinet/learn.html', {'learns': Learn.objects.all()})

def certificate(request):
    return render(request, 'cabinet/certificate.html', {'certificates': Certificate.objects.all()})

def videolearn(request): 
    return render(request, 'cabinet/video.html', {'videos': Video.objects.all()})

def commands(request):
    items = Employ.objects.all().order_by('id')
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'cabinet/commands.html', {'items': items})