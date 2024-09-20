from api.serializers.user_serializer import CustomUserSerializer
from rest_framework import viewsets,mixins, status
from user.models.user_model import CustomUserModel
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action



class CustomUserViewset(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUserModel.objects.all()
    
    
    @action(detail=False, methods=['post'])
    def create_user_with_crypt(self, request, pk=None):
        data = JSONParser().parse(request)
        password = data['password']
        serializer = CustomUserSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save(password=make_password(password))
            
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    