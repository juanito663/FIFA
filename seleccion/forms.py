from django import forms
from seleccion.models import Jugador,Equipo,Asociacion

class FormJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'


    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nacionalidad = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    posicion = forms.CharField(max_length=50)
    goles = forms.IntegerField()

class FormEquipo(forms.ModelForm):
    class Meta:
       model = Equipo
       fields = ("__all__")
    
    nombre_del_equipo = forms.CharField(required=True)
    nombre_del_entrenador = forms.CharField(required=True) 
    nombre_del_estadio =forms.CharField()
    titulos = forms.CharField()
    ciudad = forms.CharField()
    pais_de_origen = forms.CharField()

class FormAsociacion(forms.ModelForm):
    class Meta:
        model = Asociacion
        fields = ("__all__")
    
    nombre_de_la_asociacion = forms.CharField()
    pais = forms.CharField()
    nombre_del_director =forms.CharField()
    campeonato_nacional = forms.CharField()
    campeonato_internacional = forms.CharField()
    division = forms.CharField()
