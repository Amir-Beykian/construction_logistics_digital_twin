from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Supplier

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_supplier(request):
    """Allows supplier users to register their supplier locations."""
    if request.user.role != "supplier":
        return Response({"error": "Unauthorized"}, status=403)

    data = request.data
    supplier = Supplier.objects.create(
        owner=request.user,
        name=data["name"],
        location=data["location"],
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
    )

    return Response({"message": "Supplier registered successfully", "supplier_id": supplier.id})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_supplier_orders(request):
    """Returns orders assigned to a supplier."""
    if request.user.role != "supplier":
        return Response({"error": "Unauthorized"}, status=403)

    # Fetch orders from the database (placeholder example)
    orders = []  # Replace with actual queries.

    return Response({"supplier_orders": orders})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_supplier(request, supplier_id):
    """Allows supplier users to delete their supplier locations."""
    supplier = get_object_or_404(Supplier, id=supplier_id, owner=request.user)
    supplier.delete()
    return Response({"message": "Supplier deleted successfully"})