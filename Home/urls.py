from django.conf.urls import url
from Home import views


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^join/',views.join,name='join'),
    url(r'^Search/',views.search,name='search'),
]
