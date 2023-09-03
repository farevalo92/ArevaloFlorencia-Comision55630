from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils import timezone
from django.utils.decorators import method_decorator

from .models import *
from .forms import *
from datetime import datetime

import io
import matplotlib.pyplot as plt
import yfinance as yf
from django.shortcuts import get_object_or_404
import os
from django.conf import settings



from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request,"aplicacion/base.html")


def home(request):
    return render(request,"aplicacion/home.html")    

@login_required
def aboutMe(request):
    return render(request,"aplicacion/aboutMe.html")


def ver_grafico_a(request,nomenclatura,pk):
    
    try:
        accion = get_object_or_404(Acciones, nomenclatura=nomenclatura, pk=pk)
        
        data = yf.download(accion.nomenclatura, start=accion.fecha_inicio, end=datetime.today())
        

        plt.figure(figsize=(10, 6))
        plt.plot(data['Close'])
        plt.title(f'Precio de Cierre para {accion.nomenclatura}')
        plt.xlabel('Fecha')
        plt.ylabel('Precio de Cierre')
        

        img_filename = f"{nomenclatura}_grafico.png"
        img_path_accion = os.path.join(settings.MEDIA_ROOT, 'graficos', img_filename)
        plt.savefig(img_path_accion)
         
        return render (request, 'aplicacion/graficoAccion.html', {'accion':accion,'nomenclatura':nomenclatura})    
    
    except yf.YFinanceError:
        response = HttpResponse("Imagen no encontrada", content_type="text/plain")
        response.status_code = 404
        return response



class FciList(ListView):
    model = Fci
    context_object_name = 'fci_list'
 


class FciCreate(CreateView):
    model = Fci
    fields = ['nombre', 'nomenclatura', 'cuotapartes','fecha_actualizacion','ultimo_valor']
    success_url = reverse_lazy('fci')

class FciUpdate(UpdateView):
    model = Fci
    fields = ['nombre', 'nomenclatura', 'cuotapartes','fecha_actualizacion','ultimo_valor']
    success_url = reverse_lazy('fci')


class FciDelete(DeleteView):
    model = Fci
    success_url = reverse_lazy('fci')


class AccionesList(ListView):
    model = Acciones



class AccionesCreate(CreateView):
    model = Acciones
    fields = ['nombre', 'nomenclatura', 'nominales','fecha_inicio']
    success_url = reverse_lazy('acciones')


class AccionesUpdate(UpdateView):
    model = Acciones
    fields = ['nombre', 'nomenclatura', 'nominales','fecha_inicio']
    success_url = reverse_lazy('acciones')


class AccionesDelete(DeleteView):
    model = Acciones
    success_url = reverse_lazy('acciones')


class BonoList(ListView):
    model = Bono
    context_object_name = 'bono_list'


class BonoCreate(CreateView):
    model = Bono
    fields = ['nombre', 'nomenclatura', 'nominales','fecha_actualizacion','ultimo_valor']
    success_url = reverse_lazy('bonos')


class BonoUpdate(UpdateView):
    model = Bono
    fields = ['nombre', 'nomenclatura', 'nominales','fecha_actualizacion','ultimo_valor']
    success_url = reverse_lazy('bonos')


class BonoDelete(DeleteView):
    model = Bono
    success_url = reverse_lazy('bonos')




class CaucionesList(ListView):
    model = Cauciones
    context_object_name = 'cauciones_list'


class CaucionesCreate(CreateView):
    model = Cauciones
    fields = ['nombre', 'nomenclatura', 'nominales','fecha_actualizacion','ultimo_valor']
    success_url = reverse_lazy('cauciones')


class CaucionesUpdate(UpdateView):
    model = Cauciones
    fields = ['nombre', 'nomenclatura', 'nominales','fecha_actualizacion','ultimo_valor']
    success_url = reverse_lazy('cauciones')


class CaucionesDelete(DeleteView):
    model = Cauciones
    success_url = reverse_lazy('cauciones')


@login_required
def buscarFci(request):
    return render(request, "aplicacion/buscarFci.html")

@login_required
def buscarFci2(request):
    patron = request.GET['buscar']
    if patron:
        fci_list = Fci.objects.filter(nombre__icontains=patron)
        contexto= {"fci_list": fci_list, 'titulo':f'FondoComun tiene como patron "{patron}"'}
             
        return render(request, "aplicacion/fci_list.html", contexto) 
    return HttpResponse("No se ingresaron datos para buscar!")


@login_required
def buscarAccion(request):
    return render(request, "aplicacion/buscarAccion.html")

@login_required
def buscarAccion2(request):
    patron = request.GET['buscar']
    if patron:
        acciones_list = Acciones.objects.filter(nombre__icontains=patron)
        contexto= {"acciones_list": acciones_list, 'titulo':f'Acciones tiene como patron "{patron}"'}
             
        return render(request, "aplicacion/acciones_list.html", contexto) 
    return HttpResponse("No se ingresaron datos para buscar!")


@login_required
def buscarBono(request):
    return render(request, "aplicacion/buscarBono.html")

@login_required
def buscarBono2(request):
    patron = request.GET['buscar']
    if patron:
        bono_list = Bono.objects.filter(nombre__icontains=patron)
        contexto= {"bono_list": bono_list, 'titulo':f'Bonos tiene como patron "{patron}"'}
             
        return render(request, "aplicacion/bono_list.html", contexto) 
    return HttpResponse("No se ingresaron datos para buscar!")



@login_required
def buscarCaucion(request):
    return render(request, "aplicacion/buscarCaucion.html")

@login_required
def buscarCaucion2(request):
    patron = request.GET['buscar']
    if patron:
        cauciones_list = Cauciones.objects.filter(nombre__icontains=patron)
        contexto= {"cauciones_list": cauciones_list, 'titulo':f'Cauciones tiene como patron "{patron}"'}
             
        return render(request, "aplicacion/cauciones_list.html", contexto) 
    return HttpResponse("No se ingresaron datos para buscar!")






def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).avatar.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})      

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 



@login_required
def agregarModificarBorrarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) # Diferente a los forms tradicionales
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, avatar=form.cleaned_data['avatar'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            avatar = Avatar.objects.get(user=request.user.id).avatar.url
            request.session["avatar"] = avatar
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })



@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        user_form = UserEditForm(request.POST)
        avatar_form=AvatarFormulario(request.POST, request.FILES)
    
        if user_form.is_valid():
            usuario.email = user_form.cleaned_data.get('email')
            usuario.password1 = user_form.cleaned_data.get('password1')
            usuario.password2 = user_form.cleaned_data.get('password2')
            usuario.first_name = user_form.cleaned_data.get('first_name')
            usuario.last_name = user_form.cleaned_data.get('last_name')
            usuario.save()

            agregarModificarBorrarAvatar(request)

            return render(request,"aplicacion/base.html")
        else:
            return render(request,"aplicacion/editarPerfil.html", {'user_form': user_form, 'avatar_form': avatar_form, 'usuario': usuario.username})
    else:
        user_form = UserEditForm(instance=usuario)
        avatar_form=AvatarFormulario()
    return render(request, "aplicacion/editarPerfil.html", {'user_form': user_form,'avatar_form': avatar_form, 'usuario': usuario.username})
