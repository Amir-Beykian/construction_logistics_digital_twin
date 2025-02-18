from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer

User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    Returns JWT access and refresh tokens on successful registration.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]  # Allows anyone to register without authentication

    def create(self, request, *args, **kwargs):
        """
        Custom create method to generate JWT tokens after user registration.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validates input data
        user = serializer.save()
        refresh = RefreshToken.for_user(user)  # Generates JWT tokens

        return Response({
            "user_id": user.id,
            "username": user.username,
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token),
        })
