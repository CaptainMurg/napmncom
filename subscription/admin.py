from django.contrib import admin

from subscription.models import Currency, ExchangeRate, Distribution, Rate

class RateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'distribution', 'months', 'price') 

class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('currency', 'percent')

admin.site.register(Currency)
admin.site.register(ExchangeRate, ExchangeAdmin)
admin.site.register(Distribution)
admin.site.register(Rate, RateAdmin)
