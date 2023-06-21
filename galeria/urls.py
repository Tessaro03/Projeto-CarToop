from django.urls import path
from galeria.views import *

urlpatterns = [
    path("",index, name='index'),
    path('estoque', estoque, name='estoque'),
    path('produto/<int:foto_id>', produto,name='produto'),
    path('buscar',buscar,name='buscar'),
    path('filtro/<str:tipo>',filtro, name='filtro'),
    path('marca/<str:marca>',filtroMarca, name='filtroMarca'),
    path('editar-imagem/<int:foto_id>',editar_imagem,name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>',deletar_imagem,name='deletar_imagem'),
]