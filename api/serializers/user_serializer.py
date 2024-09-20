from rest_framework import serializers
from user.models.user_model import CustomUserModel

class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUserModel
        fields = ('username', 'password')
        
        