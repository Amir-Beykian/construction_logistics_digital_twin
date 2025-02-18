from rest_framework import generics, permissions
from .models import Bouwhub
from .serializers import BouwhubSerializer

class BouwhubListCreateView(generics.ListCreateAPIView):
    """
    API to list all bouwhubs or create a new bouwhub.
    """
    queryset = Bouwhub.objects.all()
    serializer_class = BouwhubSerializer
    permission_classes = [permissions.IsAuthenticated]
