from django.shortcuts import render,redirect
from seleccion.forms import FormJugador,FormEquipo,FormAsociacion
from seleccion.models import Jugador,Equipo,Asociacion
from . import forms


def index(request):
    return render(request, 'seleccion/index.html')


###########################################################################################

                                       #jugadores#

###########################################################################################   

def listadoJugadores(request):
    jugadores = Jugador.objects.all()
    data = {'jugadores': jugadores}
    return render(request, 'seleccion/jugadores.html', data)

def agregarJugadores(request):
    form = FormJugador()
    if request.method == 'POST':
        form = FormJugador(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'seleccion/agregarJugadores.html', data)

def eliminarJugadores(request, id):
    jugadores = Jugador.objects.get(id = id)
    jugadores.delete()
    return redirect('/jugadores')

def actualizarJugadores(request, id):
    jugadores = Jugador.objects.get(id = id)
    form = FormJugador(instance=jugadores)
    if request.method == 'POST':
        form = FormJugador(request.POST, instance=jugadores)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'seleccion/agregarJugadores.html', data)


###########################################################################################

                                       #equipos#

###########################################################################################   

def listadoEquipo(request):
    equipos = Equipo.objects.all()
    data = {'equipos':equipos}
    return render(request,'seleccion/equipos.html',data)


def agregarEquipo(request):
    form = FormEquipo()
    if request.method == 'POST':
        form = FormEquipo(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'seleccion/agregarEquipo.html', data)
    
def eliminarEquipo(request , id):
    equipo = Equipo.objects.get(id = id)
    equipo.delete()
    return redirect('/equipos',)

def actualizarEquipo(request, id):
    equipo = Equipo.objects.get(id = id)
    form = FormEquipo(instance=equipo)
    if request.method == 'POST':
        form = FormEquipo(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'seleccion/agregarEquipo.html', data)


###########################################################################################

                                       #asociacion#

###########################################################################################   

def listadoAsocioacion(request):
    asociaciones = Asociacion.objects.all()
    data = {'asociaciones':asociaciones}
    return render(request,'seleccion/asociaciones.html',data)


def agregarAsocioacion(request):
    form = FormAsociacion()
    if request.method == 'POST':
        form = FormAsociacion(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'seleccion/agregarAsociacion.html', data)
    
def eliminarAsociacion(request , id):
    asociacion = Asociacion.objects.get(id = id)
    asociacion.delete()
    return redirect('/asociaciones',)

def actualizarAsocioacion(request, id):
    asociaciones = Asociacion.objects.get(id = id)
    form = FormAsociacion(instance = asociaciones)
    if request.method == 'POST':
        form = FormAsociacion(request.POST, instance= asociaciones)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'seleccion/agregarAsociacion.html', data) 