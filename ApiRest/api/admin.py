from django.contrib import admin

from .models import Estado, Producto, Rol, Tienda, Usuario, Venta



# Register your models here.

#Se registran los modelos
admin.site.register(Estado)
admin.site.register(Producto)
admin.site.register(Rol)
admin.site.register(Tienda)
admin.site.register(Usuario)
admin.site.register(Venta)

