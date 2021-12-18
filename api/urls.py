from django.urls import __path__
from django.urls.conf import path
from .views import eliminar_venta, ventaview, clientesView, autosView
from .views import*

urlpatterns = [
    path('',home, name='Inicio'),



    path('ventas/',ventaview.as_view() , name='ventas'),
    path('ventas/edit/<slug:id_venta>',editar_ventaView.as_view()),
    path('ventas/edit/',editar_venta_post),
    path('ventas/eliminacionventa/<slug:venta_id>',eliminar_venta),
    path('ventas/new/',new_venta),


    path('autos',autosView.as_view(), name='autos'),
    path('edit/auto/<slug:id_especif_carro>',editar_auto, name='editar auto'),
    path('edit/auto/',editar_auto_post),
    path('autos/eliminar/<slug:id_lote>',eliminar_auto, name='eliminar auto'),
    path('autos/agregar/existente/<slug:id_lote>',agregar_existente),
    path('autos/agregar/',agregar_auto_nuevo),




    path('clientes',clientesView.as_view(), name='clientes'),
    path('create/',new_cliente),
    path('clientes/edit/<slug:id_cliente>',editar_cliente),
    path('edit/',editar_cliente_post),
    path('clientes/eliminacioncliente/<slug:id_cliente>',eliminar_cliente)
    
]