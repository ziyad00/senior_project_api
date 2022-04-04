from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'order', OrderViewSet)
router.register(r'address', AddressViewSet)
router.register(r'item', ItemViewSet)


urlpatterns = [
   path('', include(router.urls)),


]