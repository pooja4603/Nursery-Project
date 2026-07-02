from rest_framework import serializers
from .models import Plant, Pot

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class PotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pot
        fields = '__all__'