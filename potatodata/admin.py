from django.contrib import admin

from potatodata.models import ShippingPointPrice, ShippingDistrict, Variety, Grade, Package, Size, napmnRegion

class LookupAdmin(admin.ModelAdmin):
    list_display = ('usda_name','napmn_name')
    
class SPPAdmin(admin.ModelAdmin):
    list_display = ('report_date', 'shipping_district', 'season', 'variety', 'subvariety', 
        'grade', 'package', 'size', 'low', 'high', 'mostly_low', 'mostly_high', 'price_weight')

# Register your models here.
admin.site.register(ShippingDistrict,LookupAdmin)
admin.site.register(Variety,LookupAdmin)
admin.site.register(Grade,LookupAdmin)
admin.site.register(Package,LookupAdmin)
admin.site.register(Size,LookupAdmin)
admin.site.register(ShippingPointPrice,SPPAdmin)
admin.site.register(napmnRegion)
