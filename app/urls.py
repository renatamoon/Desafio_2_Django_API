from django.urls import path
from . import views


urlpatterns = [    
    path('', views.homepage, name='homepage'),
    path('perfil/<str:id>', views.perfil_usuario, name='perfil')
]