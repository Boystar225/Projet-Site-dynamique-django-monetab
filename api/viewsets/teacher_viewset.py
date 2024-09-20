from api.serializers.teacher_serializer import TeacherSerializer
from rest_framework import viewsets
from teacher.models.teacher_model import TeacherModel

class TeacherViewset(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = TeacherModel.objects.all()
    
    