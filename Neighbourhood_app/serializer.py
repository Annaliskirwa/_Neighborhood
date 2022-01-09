from rest_framework import serializers
from .models import NeighbourHood

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighbourHood
        fields = ('name', 'location', 'description','health_tell', 'police_number', 'area_administrator')