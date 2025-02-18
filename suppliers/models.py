from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Supplier(models.Model):
    """
    Represents a supplier who provides construction materials.
    """
    name = models.CharField(max_length=255)  # Supplier name
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'supplier'})  # Only suppliers can own supplier profiles
    location = models.CharField(max_length=255)  # Address of the supplier
    coordinates = models.PointField()  # GIS location (latitude, longitude)
    available_materials = models.JSONField(default=dict)  # Stores available materials (e.g., {"cement": 500, "bricks": 2000})
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
