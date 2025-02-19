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


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Supplier

@api_view(['GET'])
def supplier_locations(request):
    suppliers = Supplier.objects.all()
    data = [{"name": s.name, "latitude": s.latitude, "longitude": s.longitude} for s in suppliers]
    return Response(data)
