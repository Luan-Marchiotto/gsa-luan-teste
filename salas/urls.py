from django.urls import path
from . import views

urlpatterns = [
    path('', views.sala_list, name='sala_list'),
    path('nova/', views.sala_create, name='sala_create'),
    path('editar/<int:pk>/', views.sala_edit, name='sala_edit'),
    path('remover/<int:pk>/', views.sala_delete, name='sala_delete'),
]