from api.serializers.school_serializer import SchoolSerializer
from rest_framework import viewsets
from school.models.school_model import SchoolModel



class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()