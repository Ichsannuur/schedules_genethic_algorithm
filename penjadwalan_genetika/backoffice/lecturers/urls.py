from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^detail/(?P<id>\d+)$', views.detail, name='detail'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^active/(?P<id>\d+)$', views.active, name='active')
]
