from django.urls import path

from .views import ViewEstado, ViewProducto, ViewRol, ViewTienda, ViewUsuario, ViewVenta

urlpatterns =[
    #se importa las rutas principales de cada tabla
    path('rol/', ViewRol.as_view(), name='lista_rol'),
    path('estado/', ViewEstado.as_view(), name='lista_estado'),
    path('producto/', ViewProducto.as_view(), name='lista_producto'),
    path('tienda/', ViewTienda.as_view(), name='lista_tienda'),
    path('usuario/', ViewUsuario.as_view(), name='lista_usuario'),
    path('venta/', ViewVenta.as_view(), name='lista_venta'),

    #para buscar por id
    path('rol/<int:id>', ViewRol.as_view(), name='procesos_rol'),
    path('estado/<int:id>', ViewEstado.as_view(), name='procesos_estado'),
    path('producto/<int:id>', ViewProducto.as_view(), name='procesos_producto'),
    path('tienda/<int:id>', ViewTienda.as_view(), name='procesos_tienda'),
    path('usuario/<int:id>', ViewUsuario.as_view(), name='procesos_usuario'),
    path('venta/<int:id>', ViewVenta.as_view(), name='procesos_venta'),
]