from django.shortcuts import render
from datetime import datetime, timedelta

from potatodata.models import FWA, GRI

class FWAGRI():
    def __init__(self, napmn_region, current_price, week_diff, year_diff):
        self.napmn_region = napmn_region
        self.current_price = current_price
        self.week_diff = week_diff
        self.year_diff = year_diff

# Create your views here.
def home(request):
    context_dict = {}
    
    thisdate = FWA.objects.latest('date').date
    weekago = thisdate - timedelta(days=7)
    yearago = thisdate - timedelta(days=364)
    
    fwacurrent = FWA.objects.filter(date = thisdate)
    fwaweek = FWA.objects.filter(date = weekago)
    fwayear = FWA.objects.filter(date = yearago)
    
    gricurrent = GRI.objects.filter(date = thisdate)
    griweek = GRI.objects.filter(date = weekago)
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
                week_diff = current_price - wwa.fwa
        for ywa in fwayear:
            if ywa.napmn_region == wa.napmn_region and ywa.subvariety == wa.subvariety:
                year_diff = current_price - ywa.fwa
                
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
                week_diff = current_price - wgr.gri
        for ygr in griyear:
            if ygr.napmn_region == gr.napmn_region and ygr.subvariety == gr.subvariety:
                year_diff = current_price - ygr.gri
                
        gris.append(FWAGRI( region, current_price, week_diff, year_diff))
    
    context_dict['fwas'] = fwas
    context_dict['gris'] = gris
    context_dict['fwadate'] = thisdate
    
    return render(request, 'home.html', context_dict)