from django.db import models

# Create your models here.


class Equipo(models.Model):

    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30, blank=True)  # el campo puede                                                        # ser vacio
    twitter = models.CharField(max_length=30, unique=True)
    campeonatos = models.ManyToManyField(
        'Campeonato', through='CampeonatosEquipo')

    def __str__(self):
        return "Equipo: Nombre:%s - Siglas:%s - Twitter:%s" % (
            self.nombre,
            self.siglas,
            self.twitter)


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    numero = models.IntegerField('Numero Camiseta')
    sueldo = models.FloatField('Sueldo')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE,
                               related_name="equipo")

    def __str__(self):
        return "Jugador:Nombre: %s - Posicion: %s - Dorsal: %d \
        Sueldo: %d - Equipo(%s)" % (
            self.nombre,
            self.posicion,
            self.numero,
            self.sueldo,
            self.equipo)


class Campeonato(models.Model):

    nombre = models.CharField(max_length=30)
    auspiciante = models.CharField(max_length=30)

    equipos = models.ManyToManyField('Equipo', through='CampeonatosEquipo')

    def __str__(self):
        return "Campeonato: Nombre:%s - Auspiciante:%s" % (
            self.nombre,
            self.auspiciante)


class CampeonatosEquipo(models.Model):

    anio = models.IntegerField("Año")
    equipo = models.ForeignKey(Equipo, related_name='losequipos', 
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='loscampeonatos', 
            on_delete=models.CASCADE)
    
    def __str__(self):
        return "Informacion: Año(%d) - Equipo(%s) - Campeonato(%s)" % \
                (self.anio, self.equipo.nombre,self.campeonato.nombre)
