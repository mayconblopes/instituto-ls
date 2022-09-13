from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quem-somos/', views.quem_somos, name='quem-somos'),
    path('nosso-estudio/', views.nosso_estudio, name='nosso-estudio'),
]