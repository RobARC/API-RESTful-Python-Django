from django.db import router
from rest_framework import routers, urlpatterns
from ESWAPP.api.api import ClienteAPIViewsets, OrdenAPIViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Cliente', ClienteAPIViewsets, basename='user')
router.register(r'Orden', OrdenAPIViewsets, basename='orden')

urlpatterns = router.urls
