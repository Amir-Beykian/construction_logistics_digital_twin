from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Bouwhub(models.Model):
    """
    Represents a construction logistics hub (Bouwhub).
    Bouwhubs provide storage and transportation.
    """
    name = models.CharField(max_length=255)  # Hub name
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'bouwhub'})  # Only bouwhub users can own a hub
    location = models.CharField(max_length=255)  # Address of the hub
    coordinates = models.PointField()  # GIS location (latitude, longitude)
    storage_capacity = models.IntegerField()  # Max materials the hub can store
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
