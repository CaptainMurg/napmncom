from django.shortcuts import render
import datetime
from dateutil.relativedelta import relativedelta

from .models import PotatoLink
import potatodata.views as pdata
from potatodata.models import FWA

def home(request):
    context_dict = {}

    lastdate = FWA.objects.latest('date').date
    context_dict.update(pdata.fwagri_tables(lastdate))

    context_dict.update(pdata.idfwa_graph())
    context_dict.update(pdata.id10lb_graph())
    context_dict.update(pdata.id70s_graph())

    return render(request, 'pages/home.html', context_dict)

def about(request):
    startdate = datetime.datetime.strptime('05111992', "%d%m%Y").date()
    today = datetime.date.today()

    context_dict = {}
    context_dict['title'] = 'About'
    context_dict['years_produced'] = relativedelta(today, startdate).years

    return render(request, 'pages/about.html', context_dict)

def contact(request):
    context_dict = {}
    context_dict['title'] = 'Contact'
    context_dict['address'] = '2690 N Rough Stone Way'
    context_dict['city'] = 'Meridian'
    context_dict['state'] = 'ID'
    context_dict['zip'] = 83646
    context_dict['phone'] = '(208) 525-8397'
    context_dict['fax'] = '(208) 525-8569'
    context_dict['email'] = 'napmn@napmn.com'

    return render(request, 'pages/contact.html', context_dict)

def foblinks(request):
    links = PotatoLink.objects.filter(category__name='FOB')

    context_dict = {}
    context_dict['title'] = 'FOB Shipping Point Prices'
    context_dict['links'] = links

    return render(request, 'pages/foblinks.html', context_dict)

def terminallinks(request):
    links = PotatoLink.objects.filter(category__name='Terminal')

    context_dict = {}
    context_dict['title'] = 'Terminal Market Prices'
    context_dict['links'] = links

    return render(request, 'pages/terminallinks.html', context_dict)

def supplylinks(request):
    amslinks = PotatoLink.objects.filter(category__name='Supply/Use', subcategory__name='USDA AMS')
    nasslinks = PotatoLink.objects.filter(category__name='Supply/Use', subcategory__name='USDA NASS')
    canadalinks = PotatoLink.objects.filter(category__name='Supply/Use', subcategory__name='Canada')

    context_dict = {}
    context_dict['title'] = 'Supplies, Movement, Stocks, and Usage'
    context_dict['amslinks'] = amslinks
    context_dict['nasslinks'] = nasslinks
    context_dict['canadalinks'] = canadalinks

    return render(request, 'pages/supplylinks.html', context_dict)

def agronomylinks(request):
    links = PotatoLink.objects.filter(category__name = 'Agronomy')

    context_dict = {}
    context_dict['title'] = 'Agronomy'
    context_dict['links'] = links

    return render(request, 'pages/agronomylinks.html', context_dict)

