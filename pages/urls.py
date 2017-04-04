from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^links/fob/$', views.foblinks, name='foblinks'),
    url(r'^links/terminal/$', views.terminallinks, name='terminallinks'),
    url(r'^links/supplyuse/$', views.supplylinks, name='supplylinks'),
    url(r'^links/agronomy/$', views.agronomylinks, name='agronomylinks'),
]
