from django.shortcuts import render
import math

from subscription.models import ExchangeRate, Rate

def subscribe(request):
    context_dict = {}
    context_dict['title'] = 'Subscription Rates'
    Months = [x.months for x in Rate.objects.filter(currency__name='USD', distribution__name='Fax').order_by('-months')]
    USDFaxRates =  [float(x.price) for x in Rate.objects.filter(currency__name='USD', distribution__name='Fax').order_by('-months')]
    USDEmailRates= [float(x.price) for x in Rate.objects.filter(currency__name='USD', distribution__name='Email').order_by('-months')]
    CADFaxRates = []
    CADEmailRates=[]

    cadpercent = ExchangeRate.objects.get(currency__name='CAD').percent
    for rate in USDFaxRates:
        CADFaxRates.append(math.ceil(rate * cadpercent))
    for rate in USDEmailRates:
        CADEmailRates.append(math.ceil(rate * cadpercent))

    context_dict['Rates'] = zip(USDEmailRates, CADEmailRates, USDFaxRates, CADFaxRates, Months)

    return render(request, 'subscribe.html', context_dict)
