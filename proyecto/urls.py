from django.conf.urls import url
from . import views
from django.utils import timezone
from django.urls import path

urlpatterns = [

    url(r'^$', views.listar_vehiculo, name='listar_vehiculo'),

    url(r'^vehiculos/lista/$', views.listar_vehiculo, name='listar_vehiculo'),
    url(r'^vehiculos/new/$', views.crear_vehiculo, name='crear_vehiculo'),
    url(r'^vehiculos/detail/(?P<pk>[0-9]+)/$', views.vehiculo_detail, name='vehiculo_detail'),
    ]
