from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    """
    Serializer for suppliers.
    """
    class Meta:
        model = Supplier
        fields = '__all__'
