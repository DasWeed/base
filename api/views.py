import json

from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import DetalleVenta, EspecifCarro, Venta, Cliente, Prestamo,Direccion
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
    
def editar_venta(request,id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    return render(request,"editar_venta.html",{'venta':venta})

def editar_venta_post(request):
    id = request.POST.get('id_venta')
    print(id)
    pass







class clientesView(ListView):
    model = Cliente
    template_name = 'lista_clientes.html' 


def new_cliente(request):
    
    lastid= Cliente.objects.latest('id_cliente')
    id = lastid.id_cliente
    id = int(id[2:7])+1
    id = "CL"+str(id)
  
    


    nombre =  request.POST['txtnombrecliente']
    ap_pat = request.POST.get('txtapellidopcliente')
    ap_ma = request.POST.get('txtapellidomcliente')
    fecha = request.POST.get('fnacimiento')
    correo = request.POST.get('email')
    numero = request.POST.get('phonecliente')
    direccion = request.POST.get('numdireccion')

    ncliente = Cliente.objects.create(
        id_cliente = id,
        nombre=nombre,
        ap_paterno =ap_pat,
        ap_materno = ap_ma,
        fechanacimiento = fecha,
        correo = correo,
        telefono = numero,
        direccion_id = direccion

        
    )
  
    
    return redirect('/clientes')


#------------------------------------------------------------- EDITAR-----------------

def editar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente) #ORM 
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
    prest_cliente = Prestamo.objects.filter(cliente=id_cliente).exists() 
    print(prest_cliente)
    if prest_cliente == False:

        Dventa= Cliente.objects.get(id_cliente=id_cliente).delete()
    else:
        rest_cliente = Prestamo.objects.get(cliente=id_cliente).delete()

        Dventa= Cliente.objects.get(id_cliente=id_cliente).delete()
    return redirect('/clientes')






class autosView(ListView):  ## vista para autos 
    model =EspecifCarro
    template_name ="lista_autos.html"

def editar_auto(request, id_especif_carro):
    auto = EspecifCarro.objects.get(id_especif_carro=id_especif_carro)
    return render (request,"editar_auto.html",{'auto':auto})

def editar_auto_post(request):
    id = request.POST.get('idcarro')
    version = request.POST.get('version')
    anio = int(request.POST.get('anio'))
    print(anio)
    potencia = request.POST.get('potencia')
    modelo = request.POST.get('modelo')
    costo = request.POST.get('costo')


    Auto = EspecifCarro.objects.get(id_especif_carro=id)
    Auto.version_carro = version
    Auto.anio = anio
    Auto.hp = potencia
    Auto.modelo.nombre= modelo
    Auto.costo = costo
    Auto.save()
    return redirect('/autos')
def eliminar_auto(self):
    pass