from django.contrib import admin
from usuarios.models import Favorito

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'item',)
    list_display_links = ( 'user', 'item',)
    
   
    