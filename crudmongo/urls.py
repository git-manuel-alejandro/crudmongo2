from django.urls import path, include

urlpatterns = [
    path('', include('productos.urls')),
]
