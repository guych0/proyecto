from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .forms import ParqueoForm
from parqueos.models import Parqueo, Tipos
# Create your views here.
def lista(request):
    publi = Parqueo.objects.all()
    return render(request,'parqueos/listar_lista.html',{'publi':publi})

@login_required
def nuevo(request):

    if request.method =="POST":
        formulario = ParqueoForm(request.POST)
        if formulario.is_valid():
            parqueo=Parqueo.objects.create (nombre=formulario.cleaned_data['nombre'], fecha_inicial=formulario.cleaned_data['fecha_inicial'],fecha_salida=formulario.cleaned_data['fecha_salida'])
            for vehiculo_id in request.POST.getlist('tipos'):
                tipos=Tipos(vehiculo_id=vehiculo_id, parqueo_id=parqueo.id)
                tipos.save()
            messages.add_message(request, messages.SUCCESS, 'Ingreso Guardado Exitosamente')
    else:
        formulario=ParqueoForm()
    return render(request, 'parqueos/parqueo_editar.html', {'formulario': formulario})
