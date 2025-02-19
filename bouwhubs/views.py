from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Bouwhub

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_bouwhub(request):
    """Allows Bouwhub users to register their Bouwhub locations."""
    if request.user.role != "bouwhub":
        return Response({"error": "Unauthorized"}, status=403)

    data = request.data
    bouwhub = Bouwhub.objects.create(
        owner=request.user,
        name=data["name"],
        location=data["location"],
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
    )

    return Response({"message": "Bouwhub registered successfully", "bouwhub_id": bouwhub.id})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_bouwhub_inventory(request):
    """Returns inventory available in the Bouwhub."""
    if request.user.role != "bouwhub":
        return Response({"error": "Unauthorized"}, status=403)

    # Fetch inventory from the database (placeholder example)
    inventory = []  # Replace with actual queries.

    return Response({"bouwhub_inventory": inventory})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_bouwhub(request, bouwhub_id):
    """Allows Bouwhub users to delete their Bouwhub locations."""
    bouwhub = get_object_or_404(Bouwhub, id=bouwhub_id, owner=request.user)
    bouwhub.delete()
    return Response({"message": "Bouwhub deleted successfully"})
