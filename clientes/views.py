from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Campo pelo qual vai ser ordenado:
    ordering_fields = ['nome']

    # Campo que pode ser usado para realizar buscas:
    search_fields = ['nome', 'cpf']

    # Filtro por clientes ativos:
    filterset_fields = ['ativo']