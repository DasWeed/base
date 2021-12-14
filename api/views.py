import json

from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import DetalleVenta, EspecifCarro, Venta, Cliente, Prestamo
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


def new_cliente(request):
    id = request.POST.get('txtid_cliente')
    print("---> ID",id)
    nombre =  request.POST['txtnombrecliente']
    ap_pat = request.POST.get('txtapellidopcliente')
    ap_ma = request.POST['txtapellidomcliente']
    fecha = request.POST['fnacimiento']
    correoe = request.POST['email']
    numero = request.POST['phonecliente']
    
    return redirect('/clientes')


def editar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render (request,"edit_cliente.html",{'cliente':cliente})
#----------------------------------------------------------------un objeto para renderizar la plantilla y otro metodo para mandar los datos por un metodo POST
def editar_cliente_post (request):
    #id= request.POST['txtid_cliente']
    id = request.POST.get('txtid_cliente')
    print("---> ID",id)
    nombre =  request.POST['txtnombrecliente']
    ap_pat = request.POST.get('txtapellidopcliente')
    ap_ma = request.POST['txtapellidomcliente']
    fecha = request.POST['fnacimiento']
    correoe = request.POST['email']
    numero = request.POST['phonecliente']
    
    
    cliente= Cliente.objects.get(id_cliente=id)
    cliente.nombre = nombre
    cliente.ap_paterno = ap_pat
    cliente.ap_materno = ap_ma
    cliente.fechanacimiento = fecha
    cliente.telefono = numero
    cliente.correo =correoe
    cliente.save()
    return redirect('/clientes')

def eliminar_cliente(request,id_cliente):
    prest_cliente = Prestamo.objects.get(cliente=id_cliente).delete()  
    Dventa= Cliente.objects.get(id_cliente=id_cliente).delete()
    return redirect('/clientes')






class autosView(ListView):
    model =EspecifCarro
    template_name ="lista_autos.html"