from api.serializers.student_serializers import StudentSerializer
from rest_framework import viewsets
from student.models.student_model import StudentModel


class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = StudentModel.objects.all()