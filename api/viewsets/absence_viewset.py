from rest_framework import viewsets
from rest_framework import serializers
from api.serializers.absence_serializer import AbsenceSerializer
from student.models.absence_model import  AbsenceModel

class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = AbsenceModel.objects.all()
    serializer_class = AbsenceSerializer
