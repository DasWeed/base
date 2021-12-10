from django.urls import __path__
from django.urls.conf import path
from .views import eliminar_venta, ventaview, clientesView, autosView
from .views import*

urlpatterns = [
    path('ventas/',ventaview.as_view() , name='ventas'),
    path('ventas/<slug:id_venta>', ventaview.as_view(), name='proceso_de_venta'),
    path('',home),
    path('clientes',clientesView.as_view(), name='clientes'),
    path('autos',autosView.as_view(), name='autos'),


    path('edit/<slug:id_cliente>',editar_cliente),
    path('clientes/eliminacioncliente/<slug:id_cliente>',eliminar_cliente),
    path('ventas/eliminacionventa/<slug:venta_id>',eliminar_venta)
]