from django.contrib import admin
from django.urls import path, include
from bancos.views import * 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bancos', BancoViewset, basename='Bancos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #path('banco/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
]
