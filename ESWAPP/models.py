from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, DateTimeField, IntegerField

# Create your models here.


class Orden(models.Model):
    nro_orden = IntegerField(unique=True,  auto_created=True, null=False)
    cliente = CharField(max_length=200, blank=False, null=False)
    fecha_orden = DateTimeField(auto_now_add=False)
    SOLICITADA = 'SOL'
    APROBADA = 'APR'
    ANULADA = 'NUL'
    estado_choice = (
        (SOLICITADA, 'Solicitada'),
        (APROBADA, 'Aprobada'),
        (ANULADA, 'Anulada')
    )
    estado = CharField(max_length=20, choices=estado_choice,
                       default=SOLICITADA)

    def __str__(self):
        return self.cliente


class Cliente(models.Model):
    nombre = CharField(max_length=100, blank=True, null=False)
    Direccion = CharField(max_length=255, blank=True, null=True)
    Telefono = CharField(max_length=15, blank=True, null=False)
    Nacionalidad = CharField(max_length=100, blank=True, null=True)
    Correo = models.EmailField()
    orden = models.ForeignKey(
        Orden, null=True, related_name='ordenando', on_delete=CASCADE)

    def __str__(self):
        return self.Correo
