from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for projects.
    Converts Project model data to JSON.
    """
    class Meta:
        model = Project
        fields = '__all__'  # Includes all fields
