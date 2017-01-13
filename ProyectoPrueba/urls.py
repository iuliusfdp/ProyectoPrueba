from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ProyectoPrueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^', include('parking.urls')),
    url(r'^',  include('parking.urls', namespace="parking")),
    url(r'^admin/', include(admin.site.urls)),
]
