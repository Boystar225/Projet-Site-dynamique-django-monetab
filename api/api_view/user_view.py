from rest_framework.parsers import JSONParser
from user.models.user_model import CustomUserModel
from django.views.decorators.csrf import csrf_exempt
from  ..serializers.user_serializer import UserSerializer
from django.http import HttpResponse, JsonResponse
@csrf_exempt
def User_list(request):
    
    if request.method == 'GET':
        users = CustomUserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def user_detail(request, pk):
    try:
        user = CustomUserModel.objects.get(pk=pk)
    except CustomUserModel.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
    
    
    
    