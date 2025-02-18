from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    """
    Represents a construction project where materials are needed.
    Each project is owned by a subcontractor.
    """
    name = models.CharField(max_length=255)  # Project name
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'project'})  # Only subcontractors can own projects
    location = models.CharField(max_length=255)  # Address of the project
    latitude = models.FloatField()  # For GIS mapping
    longitude = models.FloatField()  # For GIS mapping
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
