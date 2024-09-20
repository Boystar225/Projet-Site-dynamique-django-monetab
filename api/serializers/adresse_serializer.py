from rest_framework import serializers
from base.models.helpers.adress_model import AdressModel

class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = AdressModel
        fields = '__all__'