from django.contrib.gis.db import models  # Use GIS-enabled fields
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    """
    Represents a construction project where materials are needed.
    Each project is owned by a subcontractor.
    """
    name = models.CharField(max_length=255)  # Project name
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'subcontractor'})  # Only subcontractors can own projects
    location = models.CharField(max_length=255)  # Address of the project
    coordinates = models.PointField()  # GIS location (latitude, longitude)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
