from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'napmnweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'potatodata.views.home', name='home'),
    url(r'^about/$', 'potatodata.views.about', name='about'),
    url(r'^contact/$', 'potatodata.views.contact', name='contact'),
    url(r'^subscribe/$', 'subscription.views.subscribe', name='subscribe'),
    url(r'^links/fob/$', 'potatodata.views.foblinks', name='foblinks'),
    url(r'^links/terminal/$', 'potatodata.views.terminallinks', name='terminallinks'),
    url(r'^links/supplyuse/$', 'potatodata.views.supplylinks', name='supplylinks'),
    url(r'^links/agronomy/$', 'potatodata.views.agronomylinks', name='agronomylinks'),
)
