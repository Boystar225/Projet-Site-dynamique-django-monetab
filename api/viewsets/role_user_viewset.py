from rest_framework import viewsets
from ..serializers.role_user_serializer import RoleUserSerializer
from user.models.roleUser_model import RoleUserModel

class RoleUserViewSet(viewsets.ModelViewSet):
    serializer_class = RoleUserSerializer
    queryset = RoleUserModel.objects.all()