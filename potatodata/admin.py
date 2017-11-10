from django.contrib import admin
from django.http import HttpResponse

from .models import ShippingPointPrice, ShippingDistrict, Variety, Grade, Package, Size, napmnRegion, FWA, GRI, TruckRate

# Export Functions

def export_truckrates_to_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=truckrates.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Week Ending"),
        smart_str(u"Shipping District"),
        smart_str(u"Freight Destination"),
        smart_str(u"Day Low"),
        smart_str(u"Day High"),
        smart_str(u"Week Low"),
        smart_str(u"Week High"),
        smart_str(u"Price Weight"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.week_ending),
            smart_str(obj.shipping_district),
            smart_str(obj.freight_destination),
            smart_str(obj.day_low),
            smart_str(obj.day_high),
            smart_str(obj.week_low),
            smart_str(obj.week_high),
            smart_str(obj.price_weight),
        ])
    return response
export_truckrates_to_csv.short_description = u"Export Truckrates to CSV"

# Admin Classes
class LookupAdmin(admin.ModelAdmin):
    list_display = ('usda_name','napmn_name')

class SPPAdmin(admin.ModelAdmin):
    list_display = ('report_date', 'shipping_district', 'season', 'variety', 'subvariety',
        'grade', 'package', 'size', 'low', 'high', 'mostly_low', 'mostly_high', 'price_weight')

class TruckAdmin(admin.ModelAdmin):
    list_display = ('week_ending', 'shipping_district', 'freight_destination', 'week_low', 'week_high', 'day_low', 'day_high')

    actions = [export_truckrates_to_csv]

# Register your models here.
admin.site.register(ShippingDistrict,LookupAdmin)
admin.site.register(Variety,LookupAdmin)
admin.site.register(Grade,LookupAdmin)
admin.site.register(Package,LookupAdmin)
admin.site.register(Size,LookupAdmin)
admin.site.register(ShippingPointPrice,SPPAdmin)
admin.site.register(napmnRegion)
admin.site.register(TruckRate, TruckAdmin)
# Register your models here.
