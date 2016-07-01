from django.conf.urls import url, include
from django.contrib import admin
from App import urls as gfa
from App.views import Home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hola/', include(gfa)),
    url(r'^',
        include('main.urls', namespace="main")),
]
