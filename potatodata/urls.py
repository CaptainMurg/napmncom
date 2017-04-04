from django.conf.urls import url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'napmnweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^potatodata/fwagri-tables$', views.fwagri_tables, name='fwagri-tables'),
    url(r'^potatodata/graph-idfwa$', views.idfwa_graph, name='graph-idfwa'),
    url(r'^potatodata/graph-id10lb', views.id10lb_graph, name='graph-id10lb'),
    url(r'^potatodata/graph-id70s$', views.id70s_graph, name='graph-id70s'),
]
