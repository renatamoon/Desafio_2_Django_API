from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def homepage(request):
    usuarios = Usuario.objects.all()

    form = UsuarioForm()

    if request.method =='POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')    

    context = {'usuarios': usuarios, 'form': form}
    return render(request, 'app_template/cadastro.html', context)


def perfil_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'app_template/perfil_usuario.html', {'usuario': usuario})
