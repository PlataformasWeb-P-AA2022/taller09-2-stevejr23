from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import Campeonato, CampeonatosEquipos, Equipo, Jugador

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class JugadorAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'posicion', 'numero', 'sueldo', 'equipo')
    search_fields = ('nombre', 'equipo')

admin.site.register(Jugador, JugadorAdmin)


class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'twitter')
    search_fields = ('equipo__nombre','siglas')

admin.site.register(Equipo, EquipoAdmin)


class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre','auspiciante')
    search_fields= ('equipo__nombre',)

admin.site.register(Campeonato,CampeonatoAdmin)

class CampeonatosEquiposAdmin(admin.ModelAdmin):
    list_display = ('anio','equipo','campeonato')
    search_fields= ('anio','equipo__nombre','campeonato__nombre')

admin.site.register(CampeonatosEquipos,CampeonatosEquiposAdmin)


