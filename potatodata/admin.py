from django.contrib import admin

from potatodata.models import ShippingPointPrice, ShippingDistrict, Variety, Grade, Package, Size, napmnRegion, FWA, GRI, PotatoLink, LinkCategory, LinkSubcategory, TruckRate

class LookupAdmin(admin.ModelAdmin):
    list_display = ('usda_name','napmn_name')
    
class SPPAdmin(admin.ModelAdmin):
    list_display = ('report_date', 'shipping_district', 'season', 'variety', 'subvariety', 
        'grade', 'package', 'size', 'low', 'high', 'mostly_low', 'mostly_high', 'price_weight')

class Link(admin.ModelAdmin):
    list_display = ('text', 'category', 'subcategory', 'url', 'description')

class TruckAdmin(admin.ModelAdmin):
    list_display = ('week_ending', 'shipping_district', 'freight_destination', 'week_low', 'week_high', 'day_low', 'day_high')

# Register your models here.
admin.site.register(ShippingDistrict,LookupAdmin)
admin.site.register(Variety,LookupAdmin)
admin.site.register(Grade,LookupAdmin)
admin.site.register(Package,LookupAdmin)
admin.site.register(Size,LookupAdmin)
admin.site.register(ShippingPointPrice,SPPAdmin)
admin.site.register(napmnRegion)
admin.site.register(LinkCategory)
admin.site.register(LinkSubcategory)
admin.site.register(PotatoLink)
admin.site.register(TruckRate, TruckAdmin)
# Register your models here.