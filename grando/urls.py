from django.urls import path, include
from grando import views
from .views import index,bebida_blanca,vinos,bebida_sa_nueva,formulario,Bebida_sa,vino_nuevo,agregados,buscar_vinos,buscar_vinos_en_lista,buscar_bebidas_blancas,buscar_bebidas_blancas_en_lista,buscar_bebidas_sin_alcohol,buscar_bebidas_sin_alcohol_en_lista,eliminar_vino,eliminar_bebida_blanca,eliminar_bebida_sa
from users import urls

urlpatterns = [
    path("", views.index, name="index"),
   
    path("bebida_blanca/", views.formulario, name="formulario"),
    path("pedido/", views.agregados, name="pedido"),
    path("vinos/", views.vino_nuevo, name="vino_nuevo"),
   
    path("bebida_sa/", views.bebida_sa_nueva, name="bebida_sa_nueva"),
    path("busqueda/", views.busqueda, name="busqueda"),
  
    path("register/", views.register, name="register"),
    path("buscar_vinos/", views.buscar_vinos, name="buscar_vinos"),
    path("buscar_bebidas_blancas/", views.buscar_bebidas_blancas, name="buscar_bebidas_blancas"),
    path("buscar_bebidas_sin_alcohol/", views.buscar_bebidas_sin_alcohol, name="buscar_bebidas_sin_alcohol"),
    path("eliminar_vino/", views.eliminar_vino, name="eliminar_vino"),
    path("eliminar_bebida_blanca/", views.eliminar_bebida_blanca, name="eliminar_bebida_blanca"),
    path("eliminar_bebida_sa/", views.eliminar_bebida_sa, name="eliminar_bebida_sa")
]
    

