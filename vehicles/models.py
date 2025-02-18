from django.db import models
from django.contrib.auth import get_user_model
from projects.models import Project
from suppliers.models import Supplier
from bouwhubs.models import Bouwhub

User = get_user_model()

class Vehicle(models.Model):
    """
    Represents a transport vehicle that belongs to a Project, Supplier, or Bouwhub.
    """
    VEHICLE_SIZES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    FUEL_TYPES = [
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]

    owner_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name="vehicles")
    owner_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True, related_name="vehicles")
    owner_bouwhub = models.ForeignKey(Bouwhub, on_delete=models.CASCADE, blank=True, null=True, related_name="vehicles")

    brand = models.CharField(max_length=100)  # e.g., "Mercedes", "Volvo"
    vehicle_type = models.CharField(max_length=255)  # e.g., "Truck", "Electric Van"
    size = models.CharField(max_length=10, choices=VEHICLE_SIZES)  # Small, Medium, Large
    capacity_kg = models.IntegerField()  # Load capacity in kg
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES)  # Fuel type
    availability_status = models.BooleanField(default=True)  # Whether the vehicle is available
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        location = self.owner_project or self.owner_supplier or self.owner_bouwhub
        return f"{self.brand} {self.vehicle_type} ({location.name})"
