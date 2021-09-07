from django.db.models import fields
from rest_framework import serializers
from ESWAPP.models import Cliente, Orden


class ClienteSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class OrdenSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = "__all__"
