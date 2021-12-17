# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Aval(models.Model):
    id_aval = models.CharField(primary_key=True, max_length=7)
    nombre = models.CharField(max_length=15)
    ap_paterno = models.CharField(max_length=15)
    ap_materno = models.CharField(max_length=15, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.ForeignKey('Direccion', models.DO_NOTHING)
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'aval'


class Banco(models.Model):
    id_banco = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'banco'


class Cargo(models.Model):
    id_cargo = models.CharField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cargo'


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=7)
    nombre = models.CharField(max_length=15)
    ap_paterno = models.CharField(max_length=15)
    ap_materno = models.CharField(max_length=15, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    correo = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.ForeignKey('Direccion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cliente'










class DetalleVenta(models.Model):
    venta = models.OneToOneField('Venta', models.DO_NOTHING, primary_key=True)
    lote = models.ForeignKey('Lote', models.DO_NOTHING)
    paquete = models.ForeignKey('Paquete', models.DO_NOTHING, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        unique_together = (('venta', 'lote'),)


class Direccion(models.Model):
    id_direccion = models.IntegerField(primary_key=True)
    municipio = models.CharField(max_length=30, blank=True, null=True)
    colonia = models.CharField(max_length=30, blank=True, null=True)
    calle = models.CharField(max_length=30, blank=True, null=True)
    cp = models.IntegerField()
    no_calle = models.IntegerField(blank=True, null=True)
    estado = models.ForeignKey('Estado', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    noempleado = models.CharField(primary_key=True, max_length=7)
    nombre = models.CharField(max_length=15)
    ap_paterno = models.CharField(max_length=15)
    ap_materno = models.CharField(max_length=15, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    correo = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING)
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING)
    salario = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class EspecifCarro(models.Model):
    id_especif_carro = models.CharField(primary_key=True, max_length=6)
    version_carro = models.CharField(max_length=10, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    paisimporte = models.ForeignKey('Paisimporte', models.DO_NOTHING, blank=True, null=True)
    modelo = models.ForeignKey('Modelo', models.DO_NOTHING, blank=True, null=True)
    costo = models.DecimalField(max_digits=9, decimal_places=2)
    porcentaje_comision = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especif_carro'


class Estado(models.Model):
    id_estado = models.CharField(primary_key=True, max_length=3)
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado'

class Transmision(models.Model):
    id_transmision = models.IntegerField(primary_key=True)
    transmision = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'transmision'

class Sucursal(models.Model):
    id_sucursal = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sucursal'



class Lote(models.Model):
    id_lote = models.IntegerField(primary_key=True)
    fechallegada = models.DateField()
    color = models.CharField(max_length=30, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    garantia = models.IntegerField(blank=True, null=True)
    transmision = models.ForeignKey(Transmision, models.DO_NOTHING, blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)
    especifcarro = models.ForeignKey(EspecifCarro, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lote'


class Modelo(models.Model):
    id_modelo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'modelo'


class Modopago(models.Model):
    id_modopago = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=17)

    class Meta:
        managed = False
        db_table = 'modopago'


class Paisimporte(models.Model):
    id_paisimporte = models.IntegerField(primary_key=True)
    pais = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'paisimporte'


class Paquete(models.Model):
    id_paquete = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=10)
    llantas = models.CharField(max_length=10, blank=True, null=True)
    neumaticos = models.BooleanField(blank=True, null=True)
    farosniebla = models.CharField(max_length=1, blank=True, null=True)
    ventpolarizadas = models.CharField(max_length=1, blank=True, null=True)
    interior = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paquete'


class Prestamo(models.Model):
    id_prestamo = models.CharField(primary_key=True, max_length=7)
    cantprestada = models.IntegerField()
    fechaprestamo = models.DateField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    status = models.ForeignKey('StatusPrestamo', models.DO_NOTHING)
    banco = models.ForeignKey(Banco, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestamo'


class StatusPrestamo(models.Model):
    id_status_prestamo = models.BooleanField(primary_key=True)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'status_prestamo'




class Venta(models.Model):
    id_venta = models.CharField(primary_key=True, max_length=7)
    fechacompra = models.DateField(blank=True, null=True)
    plazospagar = models.IntegerField(blank=True, null=True)
    tramplaca = models.CharField(max_length=1, blank=True, null=True)
    modopago = models.ForeignKey(Modopago, models.DO_NOTHING, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'
