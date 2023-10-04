from rest_framework import serializers
from core.user.models import User


class RegisterSerializer(serializers.ModelSerializer):
    
    """ register serializer for request and create user"""
    
    # making sure password must be atleast 8 characters long and not ready by user
    
    password = serializers.CharField(max_length=125, min_length=8, write_only=True, required=True)
    
    # list of the fields to required in the request or response
    
    class Meta:
        model = User
        fields = ['id', 'bio', 'avatar', 'email', 'username', 'first_name', 'last_name', 'password']
        
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    
    
        
    
    