from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    """
    Serializer for vehicles.
    Converts Vehicle model data to JSON.
    """

    class Meta:
        model = Vehicle
        fields = '__all__'  # Includes all fields
