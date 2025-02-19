from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@api_view(['POST'])
def register_user(request):
    """Handles user registration."""
    data = request.data
    if User.objects.filter(username=data['username']).exists():
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        username=data['username'],
        email=data['email'],
        password=make_password(data['password']),
        role=data['role']  # Assign role from request
    )

    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    """Handles user login and returns JWT tokens."""
    data = request.data
    try:
        user = User.objects.get(username=data['username'])
        if not user.check_password(data['password']):
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

    # Generate JWT tokens
    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "role": user.role
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_details(request):
    """Returns user details for authenticated users."""
    return Response({
        "username": request.user.username,
        "email": request.user.email,
        "role": request.user.role
    })
