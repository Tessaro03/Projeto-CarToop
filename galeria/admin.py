from django.contrib import admin
from galeria.models import Veiculo, Foto

class ListandoVeiculo(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'nome', 'publicada')
    list_display_links = ('id', 'tipo', 'nome')
    search_fields = ('nome',)
    list_editable = ('publicada',)

class FotoInline(admin.TabularInline):
    model = Foto

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'nome', 'publicada')
    list_display_links = ('id', 'tipo', 'nome')
    search_fields = ('nome',)
    list_editable = ('publicada',)
    inlines = [FotoInline]

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    pass