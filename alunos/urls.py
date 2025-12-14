from django.urls import path
from . import views

urlpatterns = [
    path('', views.aluno_list, name='aluno_list'),
    path('novo/', views.aluno_create, name='aluno_create'),
    path('editar/<int:pk>/', views.aluno_edit, name='aluno_edit'),
    path('remover/<int:pk>/', views.aluno_delete, name='aluno_delete'),
]