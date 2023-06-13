from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from bancos.models import Banco
from bancos.serializer import BancoSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET']


class BancoViewset(viewsets.ReadOnlyModelViewSet):
    """Exibindo todas as instituições"""
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
    permission_classes = [IsAuthenticated | ReadOnly]

    def retrieve(self, request, pk=None):
        queryset = Banco.objects.all()
        busca = (str(pk).zfill(3))
        banco = get_object_or_404(queryset, numero_codigo=busca)
        serializer = self.get_serializer(banco)
        return Response(serializer.data)




# Permitido a criação via tela 
# class BancoViewset(viewsets.ModelViewSet):
#     """Exibindo todos os bancos"""
#     queryset = Banco.objects.all()
#     serializer_class = BancoSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]