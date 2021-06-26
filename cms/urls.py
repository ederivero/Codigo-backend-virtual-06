from django.urls import path

from .views import (PlatosController, ArchivosController,
                    EliminarArchivoController)

urlpatterns = [
    path('platos', PlatosController.as_view()),
    path('subirImagen', ArchivosController.as_view()),
    path('eliminarImagen', EliminarArchivoController.as_view()),
]
