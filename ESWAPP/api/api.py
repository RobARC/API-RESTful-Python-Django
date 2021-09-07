from rest_framework import viewsets
from ESWAPP.models import Cliente, Orden
from ESWAPP.api.serializer import ClienteSerielizer, OrdenSerielizer


class ClienteAPIViewsets(viewsets.ModelViewSet):
    serializer_class = ClienteSerielizer
    queryset = Cliente.objects.all()


class OrdenAPIViewsets(viewsets.ModelViewSet):
    serializer_class = OrdenSerielizer
    queryset = Orden.objects.all()
