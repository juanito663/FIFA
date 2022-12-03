from django.contrib import admin
from seleccion.models import Jugador,Equipo,Asociacion

class JugadorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'nacionalidad', 'edad', 'posicion', 'goles']

admin.site.register(Jugador, JugadorAdmin)

class AsociacionAdmin(admin.ModelAdmin):
    list_display = ['nombre_de_la_asociacion','pais','nombre_del_director','campeonato_nacional','campeonato_internacional','division']
  
admin.site.register(Asociacion,AsociacionAdmin)

class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre_del_equipo','nombre_del_entrenador','nombre_del_estadio','titulos','ciudad','pais_de_origen']
  
admin.site.register(Equipo,EquipoAdmin)