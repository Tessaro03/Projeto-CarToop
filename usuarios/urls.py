from django.urls import path
from usuarios.views import login, cadastro, logout, favoritos, favoritar, desfavoritar

urlpatterns = [
    path("login",login, name='login'),
    path('cadastrar-se', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('favoritos',favoritos,name='favoritos'),
    path('favoritar/<int:item_id>/', favoritar, name='favoritar'),
    path('desfavoritar/<int:item_id>/', desfavoritar, name='desfavoritar'),
]