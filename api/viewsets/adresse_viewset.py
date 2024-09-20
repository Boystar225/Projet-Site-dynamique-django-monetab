from rest_framework import viewsets
from ..serializers.adresse_serializer import AdresseSerializer
from base.models.helpers.adress_model import AdressModel


class AdresseViewSet(viewsets.ModelViewSet):
    serializer_class= AdresseSerializer
    queryset = AdressModel.objects.all()