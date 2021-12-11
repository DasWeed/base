import json

from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import DetalleVenta, EspecifCarro, Venta, Cliente
from django.views.generic import ListView
from django.shortcuts import render




#  Create your views here
def home(request):
     return render(request,'index.html')



class ventaview(ListView):
    model = Venta
    template_name = 'lista_venta.html'

def eliminar_venta(request,venta_id):

    Dventa= DetalleVenta.objects.get(venta_id=venta_id).delete()
    venta= Venta.objects.get(id_venta=venta_id).delete()
        
    return redirect('/ventas')
    
def editar_venta(self,venta_id):
    pass





class clientesView(ListView):
    model = Cliente
    template_name = 'lista_clientes.html'  



def editar_cliente(request, id_cliente):
    cliente= Cliente.objects.get(id_cliente=id_cliente)
    return render (request,"edit_cliente.html",{'cliente':cliente})
 

def eliminar_cliente(request,id_cliente):

    Dventa= Cliente.objects.get(id_cliente=id_cliente).delete()
        
    return redirect('/clientes')






class autosView(ListView):
    model =EspecifCarro
    template_name ="lista_autos.html"