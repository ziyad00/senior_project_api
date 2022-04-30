from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    #user = UserSerializer()  # May be an anonymous user.

    class Meta:
        model=Profile
        fields='__all__'
   
    
class OrderSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True, source='user.id')
    
    class Meta:
        model=Order
        fields='__all__'
        #read_only_fields = ('users_like', 'total_likes')

class AddressSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True, source='user.id')
    
    class Meta:
        model=Address
        fields='__all__'
        #read_only_fields = ('users_like', 'total_likes')

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Item
        fields='__all__'
        #read_only_fields = ('users_like', 'total_likes')

