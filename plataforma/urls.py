from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.pacientes, name='pacientes'),
    path('dados_paciente/', views.dados_paciente_listar, name="dados_paciente_listar"),
    path('dados_paciente/<str:id>/', views.dados_paciente, name="dados_paciente"),
    path('grafico_peso/<str:id>/', views.grafico_peso, name="grafico_peso"),
    path('plano_alimentar_listar/', views.plano_alimentar_listar, name="plano_alimentar_listar"),
    path('plano_alimentar/<str:id>/', views.plano_alimentar, name="plano_alimentar"),
    path('refeicao/<str:id_paciente>/', views.refeicao, name="refeicao"),
    path('opcao/<str:id_paciente>/', views.opcao, name="opcao"),
    path('deletar_paciente/<str:id_paciente>', views.deletar_paciente, name='deletar_paciente'),
    # atualizar paciente
    path('editar_paciente/<int:paciente_id>', views.editar_paciente, name='editar_paciente'),
]