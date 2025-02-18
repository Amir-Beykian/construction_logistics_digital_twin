from rest_framework import generics, permissions
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleListCreateView(generics.ListCreateAPIView):
    """
    API to list or create vehicles.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API to retrieve, update, or delete a specific vehicle.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
