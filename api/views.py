import json

from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.base import TemplateView
from .models import DetalleVenta, Empleado, EspecifCarro, Modopago, Paquete, Transmision, Venta, Cliente, Prestamo,Lote, DetalleVenta, Sucursal
from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import F




#  Create your views here
def home(request):
     return render(request,'index.html')





class ventaview(TemplateView):
    #model = DetalleVenta
    template_name = 'lista_venta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dventas'] = DetalleVenta.objects.all().order_by('-venta')
        context['ventas'] = Venta.objects.all()
        context['paquetes'] = Paquete.objects.all()
        context['autos'] = EspecifCarro.objects.all()
        context['lote'] = Lote.objects.all()
        context['clientes'] = Cliente.objects.all()
        context['pago'] = Modopago.objects.all()
        context['empleado'] = Empleado.objects.all()
        return context

def eliminar_venta(request,venta_id):

    Dventa= DetalleVenta.objects.get(venta_id=venta_id).delete()
    venta= Venta.objects.get(id_venta=venta_id).delete()
        
    return redirect('/ventas')
    
class editar_ventaView(TemplateView):
    template_name = 'editar_venta.html'
    def get_context_data(self,id_venta, **kwargs):
        context = super().get_context_data(**kwargs)
        context['venta'] = Venta.objects.get(id_venta=id_venta)
        context['dventa'] = DetalleVenta.objects.get(venta_id=id_venta)
        context['empleados'] = Empleado.objects.all()
        context['modopago'] = Modopago.objects.all()
        context['lote'] = Lote.objects.all()
        return context
    pass    
    
    

def editar_venta_post(request):
    editventa = request.POST.get('idventa')
    ventanew = Venta.objects.get(id_venta=editventa)
    dventanew = DetalleVenta.objects.get(venta_id=ventanew)
    print(ventanew)
    print(dventanew)
    cliente = request.POST.get('cliente')
    cliente = Cliente.objects.get(nombre =cliente)
    
    empleado  = request.POST.get('empleado')
    
    empleado  = Empleado.objects.get(nombre =empleado)


    pago = request.POST.get('pago')[0]
    fecha = request.POST.get('fechacompra')
    placa = request.POST.get('placa')
    idlote = request.POST.get('lote')[0:5]


    print(fecha)
    print(pago)
    print("el trama de las placas es " , placa)
    print("el lote",idlote)
    print("el empleado que te atendio es ", empleado.noempleado)
    print(cliente.id_cliente)
    


    ventanew.fechacompra =fecha
    ventanew.tramplaca = placa
    ventanew.empleado = empleado
    ventanew.metodopago = pago
    ventanew.save()
    dventanew.lote_id = idlote
    dventanew.save()
    return redirect('/ventas')


def new_venta(request):
    
   
    #detalle venta
    idventa = Venta.objects.latest('id_venta')
    idventa = idventa.id_venta


    idventa = int(idventa[2:7])+1 # se utilza tanto en la tabla de detalle de venta como en la de venta 
    idventa = "VN"+str(idventa)
    paquete = request.POST.get('paquete')[0]
    unidades = request.POST.get('cantidad')
    idlote = request.POST.get('lote')[0:5]


    

    #tabla de venta

    idcliente =  request.POST.get('cliente')[0:7]
    empleado = request.POST.get('empleado')
    empleado = Empleado.objects.get(nombre=empleado)
    empleado = empleado.noempleado
    fecha = request.POST.get('fechacompra')
    placas = request.POST.get('placa')
    pago = request.POST.get('metodopago')[0]
    plazos = request.POST.get('plazospago')
    
    
    nventa = Venta.objects.create(
        id_venta =idventa,
        fechacompra = fecha,
        plazospagar = plazos,
        tramplaca = placas,
        modopago_id =pago,
        cliente_id = idcliente,
        empleado_id = empleado
    )
    ndetalleventa = DetalleVenta.objects.create(
        venta_id =str(idventa),
        lote_id =idlote,
        paquete_id =paquete,
        cantidad =unidades
    )
  

    
    return redirect('/ventas')









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
    venta = Venta.objects.filter(cliente=prest_cliente).exists()
    if prest_cliente == False :

        Dventa= Cliente.objects.get(id_cliente=id_cliente).delete()
    else:
        rest_cliente = Prestamo.objects.get(cliente=id_cliente).delete()

        Dventa= Cliente.objects.get(id_cliente=id_cliente).delete()
    return redirect('/clientes')






class autosView(TemplateView):  ## vista para autos con get context data se puede especificar mas de una tabla en vez de poner model = tabla que nos limita a trabajar sobre una sola tabla+
    template_name ="lista_autos.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lote'] = Lote.objects.all()
        context['Sucursal'] = Sucursal.objects.all()
        context['transmision'] = Transmision.objects.all()
        context['autos'] = EspecifCarro.objects.all()
        return context

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

def agregar_existente(request,id_lote):
    lote = Lote.objects.get(id_lote=id_lote)
    lote.cantidad = F('cantidad')+1
    lote.save(update_fields=['cantidad'])

    return redirect('autos')

def agregar_auto_nuevo(request):

    lastid= Lote.objects.latest('id_lote')
    id = lastid.id_lote
    id = int(id)+1
    print(id)

    cantidad =  request.POST.get('cantidad')
    fecha = request.POST.get('fecha')
    color = request.POST.get('color')
    garantia = request.POST.get('garantia')
    sucursal = request.POST['sucursal'][0]
    transmision2 =int (request.POST.get('transmision')[0])
    auto = request.POST.get('auto')[0:6]
    
    print(sucursal, "variable de tipo  ",type(sucursal))
    print(transmision2)
    print(auto)
    
    new_lote = Lote.objects.create(
        id_lote = id,
        fechallegada = fecha,
        color = color,
        cantidad = cantidad,
        garantia = garantia,
        transmision_id= transmision2,
        especifcarro_id = auto,


    )

    return redirect('autos')
    
def eliminar_auto(request,id_lote):
    Lot = Lote.objects.get(id_lote=id_lote)
    if Lot.cantidad == 0:
        Lot = Lote.objects.get(id_lote=id_lote).delete()
    else:
        Lot.cantidad -= 1
        Lot.save(update_fields=['cantidad'])
    

   
    return redirect('/autos')
    

