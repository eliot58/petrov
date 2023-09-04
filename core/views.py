from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import json
from django.utils import timezone
from datetime import date
from dateutil.relativedelta import relativedelta
from django.urls import reverse
from django.http import HttpResponseRedirect
import binascii
from json.decoder import JSONDecodeError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, JsonResponse

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
                user.diler.last_login = timezone.now()
                user.diler.save()
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
    if request.user.is_superuser:
        logout(request)
        return redirect(login_view)
    
    try:
        bonus = DilerBonus.objects.get(seller_code=request.user.diler.seller_code)
    except DilerBonus.DoesNotExist:
        bonus = DilerBonus.objects.create(seller_code=request.user.diler.seller_code)

    return render(request, 'cabinet/main.html', {'bonuses': Bonus.objects.all()[:3], 'news': New.objects.all()[:5], 'bonus': bonus})

@login_required(login_url='/login/')
def ads(request):
    if request.user.is_superuser:
        logout(request)
        return redirect(login_view)
    
    r = requests.get(f"http://176.62.187.250/service.php?s_code={request.user.diler.seller_code}")
    
    try:
        data = json.loads(r.text)
    except JSONDecodeError:
        r = requests.get(f"http://176.62.187.250/service.php?s_code={request.user.diler.seller_code}")
        data = json.loads(r.text)

    return render(request, 'cabinet/ads.html', {'ads': data})

@login_required(login_url='/login/')
def talon(request):
    if request.user.is_superuser:
        logout(request)
        return redirect(login_view)
    if request.method == "POST":
        order_name_form = OrderNameForm(request.POST)
        if order_name_form.is_valid():
            cd = order_name_form.cleaned_data
            t = 1 if cd["order_name"].strip().split("\\")[0] == 'О' else 2
            order_id = cd["order_name"].strip().split('\\')[1]
            requests.get(f'http://176.62.187.250/loadpic.php?order_id={order_id}&email={request.user.diler.email}&type={t}')
            return redirect(talon)
    else:
        order_name_form = OrderNameForm()

    return render(request, 'cabinet/talon.html', {"form": order_name_form})

def price(request):
    return render(request, 'cabinet/price.html', {'prices': Price.objects.all().order_by('zone')})

@login_required(login_url='/login/')
def cart(request):
    if request.user.is_superuser:
        logout(request)
        return redirect(login_view)
    if request.method == 'POST':
        diler = request.user.diler
        item = Store.objects.get(id=request.POST["item_id"])
        if str(item.id) in diler.cart:
            diler.cart[str(item.id)]['count'] += int(request.POST['count'])
            diler.cart[str(item.id)]['all_price'] += int(item.price_of_bonus) * int(request.POST['count'])
        else:
            diler.cart[item.id] = {
                'photo': item.photo.url,
                'title': item.title,
                'price': item.price,
                'price_of_bonus': item.price_of_bonus,
                'count': int(request.POST["count"]),
                'all_price': int(item.price_of_bonus) * int(request.POST['count'])
            }
        diler.total_price += int(item.price_of_bonus) * int(request.POST['count'])
        diler.save()
        return redirect(store)
    return render(request, 'cabinet/cart.html', {'items': request.user.diler.cart.items()})

@login_required(login_url='/login/')
def cart_item_delete(request, id):
    if request.user.is_superuser:
        logout(request)
        return redirect(login_view)
    diler = request.user.diler
    diler.total_price -= int(diler.cart[str(id)]["all_price"])
    del diler.cart[str(id)]
    diler.save()
    return redirect(cart)

@login_required(login_url='/login/')
@csrf_exempt
def cart_item_minus(request, id):
    diler = request.user.diler
    diler.cart[str(id)]["all_price"] -= diler.cart[str(id)]["price"]
    diler.cart[str(id)]["count"] -= 1
    diler.total_price -= diler.cart[str(id)]["price"]
    diler.save()
    return JsonResponse({"success": True})

@login_required(login_url='/login/')
@csrf_exempt
def cart_item_plus(request, id):
    diler = request.user.diler
    diler.cart[str(id)]["all_price"] += diler.cart[str(id)]["price"]
    diler.cart[str(id)]["count"] += 1
    diler.total_price += diler.cart[str(id)]["price"]
    diler.save()
    return JsonResponse({"success": True})


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
    if request.user.is_superuser:
        logout(request)
        return redirect(login_view)
    if request.method == 'POST':
        diler = request.user.diler
        diler.fullName = request.POST['fullName']
        diler.email = request.POST['email']
        diler.phone = request.POST['phone']
        diler.alert_phone = request.POST['alert_phone']
        diler.address = request.POST['address']
        try:
            diler.region_id  = int(request.POST['region'])
        except KeyError:
            pass
        diler.save()
        return redirect(profile)
    return render(request, 'cabinet/profile.html', {"regions": Region.objects.all()})

@login_required(login_url='/login/')
def orders(request):
    if request.user.is_superuser:
        logout(request)
        return redirect(login_view)
    
    if 'create_date_to' in request.GET:
        r = requests.get(f'http://176.62.187.250/loadDataForGridPerSellerCode.php?jsoncallback=jQuery1113010583719635799582_1676741279402&s_code={request.user.diler.seller_code}&create_date_from={request.GET["create_date_from"]}&create_date_to={request.GET["create_date_to"]}&order_id_from=&order_id_to=&manufacture_date_from=&manufacture_date_to=&ready_date_from=&ready_date_to=&filter_select_state=')
        fr = request.GET["create_date_from"]
        to = request.GET["create_date_to"]
    else:
        current_date = date.today()
        r = requests.get(f'http://176.62.187.250/loadDataForGridPerSellerCode.php?jsoncallback=jQuery1113010583719635799582_1676741279402&s_code={request.user.diler.seller_code}&create_date_from={current_date - relativedelta(months=1)}&create_date_to={current_date}&order_id_from=&order_id_to=&manufacture_date_from=&manufacture_date_to=&ready_date_from=&ready_date_to=&filter_select_state=')
        fr = current_date
        to = current_date - relativedelta(months=1)
    s = r.text
    start = s.index('(')
    end = s.rindex(')')
    json_string = s[start+1:end]

    return render(request, 'cabinet/orders.html', {"orders": json_string, "from": fr, "to": to})

@login_required(login_url='/login/')
def store(request):
    if request.user.is_superuser:
        logout(request)
        return redirect(login_view)
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
    if request.user.is_superuser:
        logout(request)
        return redirect(login_view)
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
    items = ShapeSystem.objects.all().order_by('id')
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
    return render(request, 'cabinet/commands.html', {'director': Employ.objects.get(role="director"), 'dev': Employ.objects.get(role="development"), 'service': Employ.objects.get(role="service"), 'pricer': Employ.objects.get(role="pricer")})


def notwork(request):
    return render(request, "cabinet/notwork.html")


def ads_create(request, order_name):
    if request.method == 'POST':
        comment = request.POST["comment"]
        order_name = request.POST["order_name"]
        file_urls = []
        query = f"exec pg_create_servicedoc_for_lk_filevarchar '{request.user.diler.seller_code}', '{order_name}', '{comment}', '{request.user.username}'"
        if "file1" in request.FILES:
            file_urls.append("'" + request.FILES["file1"].name + "'")
            file_urls.append("'0x" + binascii.hexlify(request.FILES["file1"].read()).decode() + "'")
        if "file2" in request.FILES:
            file_urls.append("'" + request.FILES["file2"].name + "'")
            file_urls.append("'0x" + binascii.hexlify(request.FILES["file2"].read()).decode() + "'")
        if "file3" in request.FILES:
            file_urls.append("'" + request.FILES["file3"].name + "'")
            file_urls.append("'0x" + binascii.hexlify(request.FILES["file3"].read()).decode() + "'")
        if "file4" in request.FILES:
            file_urls.append("'" + request.FILES["file4"].name + "'")
            file_urls.append("'0x" + binascii.hexlify(request.FILES["file4"].read()).decode() + "'")
        if "file5" in request.FILES:
            file_urls.append("'" + request.FILES["file5"].name + "'")
            file_urls.append("'0x" + binascii.hexlify(request.FILES["file5"].read()).decode() + "'")
        
        requests.post(f'http://176.62.187.250/createService.php', data={"query": query + ", " + ", ".join(file_urls)})

        with open("text.txt", "w") as f:
            f.write(query + ", " + ", ".join(file_urls))
        
        return redirect(ads)
    return render(request, "cabinet/ads-create.html", {"order_name": order_name})


def ads_id(request):
    if request.method == 'POST':
        order_name_form = OrderNameForm(request.POST)
        try:
            if order_name_form.is_valid():
                cd = order_name_form.cleaned_data
                return HttpResponseRedirect(reverse("ads-create", args=[cd["order_name"]]))
        except JSONDecodeError:
            if order_name_form.is_valid():
                cd = order_name_form.cleaned_data
                return HttpResponseRedirect(reverse("ads-create", args=[cd["order_name"]]))
    else:
        order_name_form = OrderNameForm()
    return render(request, "cabinet/ads-id.html", {"form": order_name_form})


def buy(request):
    diler = request.user.diler

    bonus = DilerBonus.objects.get(seller_code=request.user.diler.seller_code)
    if bonus.total_bonus >= diler.total_price:
        bonus.total_bonus -= diler.total_price
        bonus.save()
    
        m = f'Дилер {diler.fullName}\nСделал заказ из магазина товаров:\n'

        for key, value in diler.cart.items():
            m = m + value["title"] + str(value["count"]) + " шт" + "\n"
            item = Store.objects.get(id=key)
            item.count -= int(value["count"])
            item.save()

        diler.cart = {}
        diler.total_price = 0
        diler.save()

        try:
            requests.post('https://api.telegram.org/bot5852658863:AAHezP9l75ukvpQHSD3Bt5x24kMETAeqDfY/sendMessage', json={'chat_id': '222189723', 'text': m})
        except Exception as e:
            print(e)
    return redirect(cart)

def clear_cart(request):
    diler = request.user.diler
    diler.cart = {}
    diler.total_price = 0
    diler.save()
    return redirect(cart)