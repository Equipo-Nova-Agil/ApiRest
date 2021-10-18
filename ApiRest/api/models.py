from django.db import models

# Create your models here.

#Se crean los modelos como las tablas de la base de datos
class Estado(models.Model):
    id_estado=models.IntegerField(primary_key=True)
    estado=models.CharField(max_length=30)

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    rol_usuario = models.CharField(max_length=20)


class Usuario(models.Model):
    id_usuarios = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    edad = models.IntegerField(null=True)
    genero = models.CharField(max_length=1)
    correo = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateField()
    tipo = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)
    password = models.CharField(max_length=45)
    id_rol = models.ForeignKey(Rol,
                              on_delete= models.CASCADE)
    id_estado = models.ForeignKey(Estado,
                                 on_delete= models.CASCADE)

class Tienda(models.Model):
    id_tienda = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, unique=True)
    direccion = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20)
    responsable = models.CharField(max_length=45)
    password = models.CharField(max_length=45)


class Producto(models.Model):
    id_producto = models.IntegerField( primary_key=True)
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45)
    precio = models.FloatField()
    seccion = models.CharField(max_length=45)


class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.FloatField()
