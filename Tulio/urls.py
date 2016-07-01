from django.conf.urls import url, include
from django.contrib import admin
from App import urls as gfa

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hola/', include(gfa)),
]
