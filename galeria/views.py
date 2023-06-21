from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from galeria.models import Veiculo
from galeria.forms import VeiculoForms
from usuarios.models import Favorito


def index(request):
    return render(request,"index.html")

def estoque(request):
    veiculos = Veiculo.objects.filter(publicada=True)
    paginator = Paginator(veiculos, 8)
    page = request.GET.get('page')
    veiculos_por_page = paginator.get_page(page)
    if request.user.is_authenticated:
        veiculos_favoritados = Favorito.objects.filter(user=request.user).values_list('item', flat=True)
        return render(request, 'estoque.html', {'cards': veiculos_por_page, 'veiculos_favoritados': veiculos_favoritados})
    else:
        return render(request, 'estoque.html', {'cards': veiculos_por_page})


def produto(request, foto_id):
    veiculo = get_object_or_404(Veiculo, pk=foto_id)
    if request.user.is_authenticated:
        veiculos_favoritados = Favorito.objects.filter(user=request.user).values_list('item', flat=True)
        return render(request, "produto.html", {'veiculo': veiculo,'veiculos_favoritados': veiculos_favoritados })
    else:
        return render(request, "produto.html", {'veiculo': veiculo})

def buscar(request):
    veiculos = Veiculo.objects.filter(publicada=True)
    if "buscar" in request.GET:
        buscador = request.GET['buscar']
        if buscador:
            veiculos = Veiculo.objects.filter(nome__icontains=buscador)
        if request.user.is_authenticated:
            veiculos_favoritados = Favorito.objects.filter(user=request.user).values_list('item', flat=True)
            return render(request, 'estoque.html', {'cards': veiculos   , 'veiculos_favoritados': veiculos_favoritados})
        else:
            return render(request, 'estoque.html', {'cards': veiculos})
    return render(request,"estoque.html",{"cards":veiculos})

def filtro(request, tipo):
    veiculos = Veiculo.objects.order_by("nome").filter(publicada=True, tipo=tipo)
    return render(request,'estoque.html',{'cards':veiculos})

def filtroMarca(request, marca):
    veiculos = Veiculo.objects.order_by("nome").filter(publicada=True, marca=marca)
    return render(request,'estoque.html',{'cards':veiculos})

def editar_imagem(request, foto_id):
    veiculos = Veiculo.objects.get(id=foto_id)
    form = VeiculoForms(request.POST, request.FILES, instance=veiculos)

    if form.is_valid():
        form.save()
        return redirect('estoque.html')
    return render (request,'editar_imagem.html',{'form':form ,'foto_id':foto_id})

def deletar_imagem(request, foto_id):
    veiculo = Veiculo.objects.get(id=foto_id)
    veiculo.delete()
    return redirect('estoque.html')

