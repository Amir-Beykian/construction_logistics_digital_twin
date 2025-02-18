from rest_framework import generics, permissions
from .models import Supplier
from .serializers import SupplierSerializer

class SupplierListCreateView(generics.ListCreateAPIView):
    """
    API to list all suppliers or create a new supplier.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]
