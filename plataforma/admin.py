from django.contrib import admin
from .models import Pacientes, DadosPaciente
# Register your models here.

class PacientesAdmin(admin.ModelAdmin):
    list_display = ['id','nome', 'idade', 'telefone', 'nutri']

class DadosPacienteAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'data', 'peso', 'altura']

admin.site.register(Pacientes, PacientesAdmin)
admin.site.register(DadosPaciente, DadosPacienteAdmin)