from django.conf.urls import url

from book import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^index/$', views.index, name='index')
]