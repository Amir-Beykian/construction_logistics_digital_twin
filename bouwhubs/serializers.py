from rest_framework import serializers
from .models import Bouwhub

class BouwhubSerializer(serializers.ModelSerializer):
    """
    Serializer for bouwhubs.
    """
    class Meta:
        model = Bouwhub
        fields = '__all__'
