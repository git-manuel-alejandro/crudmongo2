from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista'),
    path('nuevo/', views.crear_producto, name='crear'),
    path('editar/<str:producto_id>/', views.editar_producto, name='editar'),
    path('eliminar/<str:producto_id>/', views.eliminar_producto, name='eliminar'),
]
