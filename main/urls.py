from django.conf.urls import url
from . import views

urlpatterns = [
       url(r'^$', views.indexView.as_view(), name='index'),
       url(r'^jobs/$', views.jobsView.as_view(), name='jobs'),
       url(r'^ofertas/$', views.ofreceView.as_view(), name='ofertas'),
]
