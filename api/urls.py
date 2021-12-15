from django.urls import __path__
from django.urls.conf import path
from .views import eliminar_venta, ventaview, clientesView, autosView
from .views import*

urlpatterns = [
    path('ventas/',ventaview.as_view() , name='ventas'),
    path('ventas/<slug:id_venta>', ventaview.as_view(), name='proceso_de_venta'),
    path('',home, name='Inicio'),
    path('ventas/edit/<slug:id_venta>',editar_venta),
    path('ventas/editar',editar_venta_post),

    
    path('clientes',clientesView.as_view(), name='clientes'),



    path('autos',autosView.as_view(), name='autos'),
    path('edit/auto/<slug:id_especif_carro>',editar_auto, name='editar auto'),
    path('edit/auto/',editar_auto_post),

    path('create/',new_cliente),
    path('clientes/edit/<slug:id_cliente>',editar_cliente),
    path('edit/',editar_cliente_post),
    path('clientes/eliminacioncliente/<slug:id_cliente>',eliminar_cliente),
    
    
    path('edit/<slug:venta_id>',editar_venta),
    path('ventas/eliminacionventa/<slug:venta_id>',eliminar_venta)
]