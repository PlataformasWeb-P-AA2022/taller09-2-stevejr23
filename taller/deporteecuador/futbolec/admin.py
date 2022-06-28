from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import Campeonato, CampeonatosEquipo, Equipo, Jugador

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'numero', 'sueldo', 'equipo')
    search_fields = ('nombre', 'equipo')

admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Equipo)
admin.site.register(Campeonato)

class CampeonatosEquiposAdmin(admin.ModelAdmin):
    list_display = ('anio','equipo','campeonato')
    search_fields= ('anio','equipo__nombre','campeonato__nombre')

admin.site.register(CampeonatosEquipo,CampeonatosEquiposAdmin)


