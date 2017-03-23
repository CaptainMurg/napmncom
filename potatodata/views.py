from django.shortcuts import render

import datetime
from dateutil.relativedelta import relativedelta

from potatodata.models import FWA, GRI, ShippingPointPrice, PotatoLink

GRAPH_SUBV = "BURBANK"

class FWAGRI():
    def __init__(self, napmn_region, current_price, week_diff, year_diff):
        self.napmn_region = napmn_region
        self.current_price = current_price
        self.week_diff = week_diff
        self.year_diff = year_diff

# Views
def home(request):
    context_dict = {}

    lastdate = FWA.objects.latest('date').date
    context_dict.update(fwagri_chart(lastdate))

    context_dict.update(idfwa_graph())
    context_dict.update(id10lb_graph())
    context_dict.update(id70s_graph())

    return render(request, 'home.html', context_dict)

def about(request):
    startdate = datetime.datetime.strptime('05111992', "%d%m%Y").date()
    today = datetime.date.today()

    context_dict = {}
    context_dict['title'] = 'About'
    context_dict['years_produced'] = relativedelta(today, startdate).years

    return render(request, 'about.html', context_dict)

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

    return render(request, 'contact.html', context_dict)

def foblinks(request):
    links = PotatoLink.objects.filter(category__name='FOB')

    context_dict = {}
    context_dict['title'] = 'FOB Shipping Point Prices'
    context_dict['links'] = links

    return render(request, 'foblinks.html', context_dict)

def terminallinks(request):
    links = PotatoLink.objects.filter(category__name='Terminal')

    context_dict = {}
    context_dict['title'] = 'Terminal Market Prices'
    context_dict['links'] = links

    return render(request, 'terminallinks.html', context_dict)

def supplylinks(request):
    amslinks = PotatoLink.objects.filter(category__name='Supply/Use', subcategory__name='USDA AMS')
    nasslinks = PotatoLink.objects.filter(category__name='Supply/Use', subcategory__name='USDA NASS')
    canadalinks = PotatoLink.objects.filter(category__name='Supply/Use', subcategory__name='Canada')

    context_dict = {}
    context_dict['title'] = 'Supplies, Movement, Stocks, and Usage'
    context_dict['amslinks'] = amslinks
    context_dict['nasslinks'] = nasslinks
    context_dict['canadalinks'] = canadalinks

    return render(request, 'supplylinks.html', context_dict)

def agronomylinks(request):
    links = PotatoLink.objects.filter(category__name = 'Agronomy')

    context_dict = {}
    context_dict['title'] = 'Agronomy'
    context_dict['links'] = links

    return render(request, 'agronomylinks.html', context_dict)

# Data Collection Functions:

def fwagri_chart(thisdate):
    context_dict = {}
    
    fwacurrent = FWA.objects.filter(date = thisdate)
    gricurrent = GRI.objects.filter(date = thisdate)
    
    fwaweek = []
    x = 0
    i = 1
    while not fwaweek and x < 3:
        fwaweek = FWA.objects.filter(date = thisdate - relativedelta(days=(7 + x)))
        if not fwaweek:
            x += i
            i = -(i + i//abs(i))
    weekago = thisdate - relativedelta(days=(7 + x))
    griweek = GRI.objects.filter(date = weekago)
    
    fwayear = []
    x = 0
    i = 1
    while not fwayear and x < 3:
        fwayear = FWA.objects.filter(date = thisdate - relativedelta(days=(364 + x)))
        if not fwayear:
            x += i
            i = -(i + i//abs(i))
    yearago = thisdate - relativedelta(days=(364 + x))
    griyear = GRI.objects.filter(date = yearago)
    
    fwas = []
    
    for wa in fwacurrent:
        region = str(wa.napmn_region)
        if region == 'Idaho':
            subvariety = 'Burbank'
            if str(wa.subvariety) == 'NORKOTAH':
                subvariety = 'Norkotah'
            region = 'Idaho {}'.format(subvariety)
        current_price = wa.fwa
        week_diff = '-NA-'
        year_diff = '-NA-'
        
        for wwa in fwaweek:
            if wwa.napmn_region == wa.napmn_region and wwa.subvariety == wa.subvariety:
                week_diff = wwa.fwa
        for ywa in fwayear:
            if ywa.napmn_region == wa.napmn_region and ywa.subvariety == wa.subvariety:
                year_diff = ywa.fwa
                
        fwas.append(FWAGRI(region, current_price, week_diff, year_diff))
    
    gris = []
    
    for gr in gricurrent:
        region = str(gr.napmn_region)
        if region == 'Idaho':
            subvariety = 'Burbank'
            if str(gr.subvariety) == 'NORKOTAH':
                subvariety = 'Norkotah'
            region = 'Idaho {}'.format(subvariety)
        current_price = gr.gri
        week_diff = '-NA-'
        year_diff = '-NA-'
        
        for wgr in griweek:
            if wgr.napmn_region == gr.napmn_region and wgr.subvariety == gr.subvariety:
                week_diff = wgr.gri
        for ygr in griyear:
            if ygr.napmn_region == gr.napmn_region and ygr.subvariety == gr.subvariety:
                year_diff = ygr.gri
                
        gris.append(FWAGRI( region, current_price, week_diff, year_diff))
    
    context_dict['fwagrichart_fwas'] = fwas
    context_dict['fwagrichart_gris'] = gris
    context_dict['fwagrichart_date'] = [thisdate, weekago, yearago]

    return context_dict

def idfwa_graph():
    context_dict = {}
    subv = GRAPH_SUBV

    lastdate = FWA.objects.latest('date').date
    startdate = lastdate - relativedelta(days = 22)
    lastyear = lastdate - relativedelta(days = 364)
    startyear = lastyear - relativedelta(days = 22)
    currentfwas = FWA.objects.filter(date__gte = startdate, date__lte = lastdate, napmn_region__napmn_name = 'Idaho', subvariety__usda_name = subv)
    lastyearfwas = FWA.objects.filter(date__gte = startyear, date__lte = lastyear, napmn_region__napmn_name = 'Idaho', subvariety__usda_name = subv)

    context_dict['idfwa_thisyear'] = "{:%Y}".format(lastdate)
    context_dict['idfwa_lastyear'] = "{:%Y}".format(lastyear)
    context_dict['idfwa_thisfwas'] = [['{:%Y-%m-%d}'.format(x.date),float(x.fwa)] for x in currentfwas]
    context_dict['idfwa_lastfwas'] = [['{:%Y-%m-%d}'.format(x.date + relativedelta(days=364)),float(x.fwa)] for x in lastyearfwas]

    return context_dict

def id10lb_graph():
    context_dict = {}
    subv = GRAPH_SUBV

    lastdate = FWA.objects.latest('date').date
    startdate = lastdate - relativedelta(days = 22)
    lastyear = lastdate - relativedelta(days = 364)
    startyear = lastyear - relativedelta(days = 22)

    current10lb = ShippingPointPrice.objects.filter(report_date__gte=startdate, report_date__lte=lastdate, grade__usda_name='U.S. One 2" or 4-oz Min', package__usda_name='baled 5 10-lb film bags', shipping_district__napmn_name__napmn_name='Idaho', subvariety__usda_name = subv)
    lastyear10lb = ShippingPointPrice.objects.filter(report_date__gte=startyear, report_date__lte=lastyear, grade__usda_name='U.S. One 2" or 4-oz Min', package__usda_name='baled 5 10-lb film bags', shipping_district__napmn_name__napmn_name='Idaho', subvariety__usda_name=subv)

    context_dict['id10lb_thisyear'] = "{:%Y}".format(lastdate)
    context_dict['id10lb_lastyear'] = "{:%Y}".format(lastyear)
    context_dict['id10lb_this10lb'] = [['{:%Y-%m-%d}'.format(x.report_date),float(x.get_cwt_price())] for x in current10lb]
    context_dict['id10lb_last10lb'] = [['{:%Y-%m-%d}'.format(x.report_date + relativedelta(days=364)),float(x.get_cwt_price())] for x in lastyear10lb]

    return context_dict

def id70s_graph():
    context_dict = {}
    subv = GRAPH_SUBV

    lastdate = FWA.objects.latest('date').date
    startdate = lastdate - relativedelta(days = 22)
    lastyear = lastdate - relativedelta(days = 364)
    startyear = lastyear - relativedelta(days = 22)

    current70s = ShippingPointPrice.objects.filter(report_date__gte=startdate, report_date__lte=lastdate, size__usda_name='70s', shipping_district__napmn_name__napmn_name='Idaho', subvariety__usda_name = subv)
    lastyear70s = ShippingPointPrice.objects.filter(report_date__gte=startyear, report_date__lte=lastyear, size__usda_name='70s', shipping_district__napmn_name__napmn_name='Idaho', subvariety__usda_name=subv)

    context_dict['id70s_thisyear'] = "{:%Y}".format(lastdate)
    context_dict['id70s_lastyear'] = "{:%Y}".format(lastyear)
    context_dict['id70s_this70s'] = [['{:%Y-%m-%d}'.format(x.report_date),float(x.get_cwt_price())] for x in current70s]
    context_dict['id70s_last70s'] = [['{:%Y-%m-%d}'.format(x.report_date + relativedelta(days=364)),float(x.get_cwt_price())] for x in lastyear70s]

    return context_dict