from cgitb import lookup
from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from .serializers import *
# Create your views here.
from django.conf import settings
from django.contrib.auth.models import User

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = 'user__username'


    
    
    def perform_create(self, serializer):
        user=self.request.user
        serializer =serializer.save(user=user)

        
    def get_permissions(self):        
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Profile.objects.all()
        if self.action == 'list':
            type = self.request.query_params.get('type', None)
        if type is not None:
            # profileID = Profile.objects.get(type=type)
            queryset = queryset.filter(Type=type)
        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    
 
    #def perform_create(self, serializer):
     #   user=self.request.user
      #  serializer =serializer.save(user=user)

        
    def get_permissions(self):        
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    
 
    def perform_create(self, serializer):
        user=self.request.user
        serializer =serializer.save(user=user)

        
    def get_permissions(self):        
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    
 
    def perform_create(self, serializer):
        user=self.request.user
        serializer =serializer.save(user=user)

        
    def get_permissions(self):        
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    def get_queryset(self):
        queryset = Item.objects.all()
        if self.action == 'list':
            username = self.request.query_params.get('username', None)
            if username is not None:
                userID = User.objects.get(username=username)
                queryset = queryset.filter(user=userID)
        return queryset