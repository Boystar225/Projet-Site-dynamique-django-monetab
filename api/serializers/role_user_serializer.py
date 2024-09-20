from rest_framework import serializers
from user.models.roleUser_model import RoleUserModel

class RoleUserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = RoleUserModel
        fields = "__all__"