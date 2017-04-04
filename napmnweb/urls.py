from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'napmnweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^', include('pages.urls')),
    url(r'^potatodata/', include('potatodata.urls')),
    url(r'^subscription/', include('subscription.urls')),
]
