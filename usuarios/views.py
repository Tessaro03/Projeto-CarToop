from django.shortcuts import render, redirect, get_object_or_404
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from usuarios.models import Favorito
from galeria.models import Veiculo

from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form['senha_1'].value() != form['senha_2'].value():
            return redirect ('cadastro')
        
        nome = form['nome_cadastro'].value()
        email = form['email'].value()
        senha = form['senha_2'].value()

        if User.objects.filter(username=nome).exists():
            return redirect(cadastro)

        usuario = User.objects.create_user(
            username= nome,
            email= email,
            password= senha,
        )
        usuario.save
        return redirect("login")
    return render(request,'usuarios/cadastro.html',{'form':form})


def logout(request):
    auth.logout(request)
    messages.success(request,'Logou Feito!')
    return redirect('login')

def favoritos(request):
    favoritos = Favorito.objects.filter(user=request.user)
    veiculos_favoritados = [favorito.item for favorito in favoritos]
    return render(request, 'favoritos.html',  {'veiculos_favoritados': veiculos_favoritados})

def favoritar(request, item_id):
    item = get_object_or_404(Veiculo, pk=item_id)
    Favorito.objects.get_or_create(user=request.user, item=item)
    current_url = request.META.get('HTTP_REFERER')
    return redirect(current_url)

def desfavoritar(request, item_id):
    item = get_object_or_404(Veiculo, pk=item_id)
    Favorito.objects.filter(user=request.user, item=item).delete()
    current_url = request.META.get('HTTP_REFERER')
    return redirect(current_url)