from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@api_view(['POST'])
def register_user(request):
    """Registers a new user (Project, Supplier, Bouwhub, or Admin)."""
    data = request.data
    if User.objects.filter(username=data['username']).exists():
        return Response({"error": "Username already exists"}, status=400)

    user = User.objects.create(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        role=data['role']  # Project, Supplier, Bouwhub, Admin
    )

    return Response({"message": "User registered successfully"}, status=201)


@api_view(['POST'])
def login_user(request):
    """Logs in the user and returns JWT tokens."""
    data = request.data
    try:
        user = User.objects.get(username=data['username'])
        if user.password != data['password']:
            return Response({"error": "Invalid credentials"}, status=400)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=400)

    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "role": user.role
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_details(request):
    """Returns authenticated user details."""
    return Response({
        "username": request.user.username,
        "email": request.user.email,
        "role": request.user.role
    })
