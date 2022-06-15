from django.db import models

# Create your models here.

class Equipo(models.Model):
    
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30, blank=True)  # el campo puede 
                                                            # ser vacio
    usernameTwitter = models.CharField(max_length=30, unique=True)
    

    def __str__(self):
        return "%s - siglas: %s - twitter: %s" % (
                self.nombre,
                self.siglas,
                self.usernameTwitter)


class Jugador(models.Model):
    """
    """
    nombre = models.CharField(max_length=30) 
    posicion = models.CharField(max_length=30) 
    numero = models.IntegerField("Numero Camiseta") 
    sueldo = models.IntegerField("Sueldo") 
    equipo = models.ForeignKey(Equipo, related_name='equipos', 
            on_delete=models.CASCADE)
    
    # estudiantes = models.ManyToManyField(Estudiante, through='Matricula')

    def __str__(self):
        return "%s - posicion: %s - dorsal: %d - sueldo: %d - Equipo(%s)" % (
                self.nombre,
                self.posicion,
                self.numero,
                self.sueldo,
                self.equipo.nombre)


class Campeonato(models.Model):
    """
    """
    nombre = models.CharField(max_length=30) 
    auspiciante = models.CharField(max_length=30) 

    def __str__(self):
        return "%s - %s" % \
                (self.nombre, self.auspiciante)

class CampeonatosEquipos(models.Model):
    """
    """
    anio = models.IntegerField("Año")
    equipo = models.ForeignKey(Equipo, related_name='equipos', 
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='campeonatos', 
            on_delete=models.CASCADE)
    
    def __str__(self):
        return "Informacion: Anio(%d) - Equipo(%s) - Campeonato(%s)" % \
                (self.anio, self.equipo.nombre,self.campeonato.nombre)
    
