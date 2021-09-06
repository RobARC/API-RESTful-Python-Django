from django.contrib import admin

# Register your models here.
from .models import Cliente, Orden

admin.site.register(Cliente)
admin.site.register(Orden)
