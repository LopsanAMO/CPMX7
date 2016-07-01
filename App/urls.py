from django.conf.urls import url, include
from django.contrib import admin
from .views import Enviar 

urlpatterns = [
    url(r'^no/', Enviar.as_view()),
]
