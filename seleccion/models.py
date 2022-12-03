from django.db import models

###########################################################################################

                                       #clase jugadores#

###########################################################################################    


class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=50)
    goles = models.IntegerField()
    

    def mostrar_capitan(self):
        return "{}".format(self.nombre)

    def __str__(self):
        return self.mostrar_capitan()



###########################################################################################

                                       #clase equipo#

###########################################################################################    


class Equipo(models.Model):
    nombre_del_equipo = models.CharField(max_length=20)
    nombre_del_entrenador = models.CharField(max_length=20)
    nombre_del_estadio = models.CharField(max_length=20)
    titulos = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    pais_de_origen = models.CharField(max_length=20)
    capitan = models.ForeignKey(Jugador,null=True,blank=True, on_delete=models.CASCADE)  

    def mostrar_equipos(self):
        return "{}".format(self.nombre_del_equipo)

    def __str__(self):
        return self.mostrar_equipos()




    


###########################################################################################

                                       #clase asosiacion#

###########################################################################################    
class Asociacion(models.Model):
    nombre_de_la_asociacion = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    nombre_del_director = models.CharField(max_length=20)
    campeonato_nacional = models.CharField(max_length=20)
    campeonato_internacional = models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    equipos = models.ForeignKey(Equipo,null=True,blank=True, on_delete=models.CASCADE)  