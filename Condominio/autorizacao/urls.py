from django.urls import path
from . import views

urlpatterns = [
    path('autorizacao/', views.autorizar, name="autorizacao"),
    #path('', views.autorizar, name='autorizacao'), 
    path('', views.listar_condominios, name="listar_condominios"), 
]
