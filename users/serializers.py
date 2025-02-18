from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()  # Fetches the custom User model

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Handles creating a new user with a hashed password.
    """
    password = serializers.CharField(write_only=True)  # Ensures password is not exposed in responses

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role', 'company_name', 'location')

    def create(self, validated_data):
        """
        Creates a new user with a hashed password.
        """
        user = User.objects.create_user(**validated_data)
        return user
