from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.index),
    path('crear', views.crear_post),
    path('detalle/<int:identificador>', views.detalle_post, name='detalle_post'),
    path('editar/<int:identificador>', views.editar_post, name='editar_post'),
    path('eliminar/<int:identificador>', views.eliminar_post, name='eliminar_post'),
    path('confirmar_eliminacion/<int:identificador>', views.confirmar_eliminacion, name='confirmar_eliminacion_post'),
]