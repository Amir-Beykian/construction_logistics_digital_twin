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


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bouwhub

@api_view(['GET'])
def bouwhub_locations(request):
    bouwhubs = Bouwhub.objects.all()
    data = [{"name": b.name, "latitude": b.latitude, "longitude": b.longitude} for b in bouwhubs]
    return Response(data)
