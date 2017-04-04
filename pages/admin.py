from django.contrib import admin

from .models import PotatoLink, LinkCategory, LinkSubcategory

class Link(admin.ModelAdmin):
    list_display = ('text', 'category', 'subcategory', 'url', 'description')

# Register your models here.
admin.site.register(LinkCategory)
admin.site.register(LinkSubcategory)
admin.site.register(PotatoLink)
