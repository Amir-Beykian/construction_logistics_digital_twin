from django.contrib.auth.models import AbstractUser  # Extends Django's built-in User model
from django.db import models

class User(AbstractUser):
    """
    Custom User model that extends Django's built-in AbstractUser.
    Adds role-based authentication and company details.
    """
    # Define user roles
    USER_ROLES = [
        ('project', 'project'),
        ('supplier', 'Supplier'),
        ('bouwhub', 'Bouwhub'),
    ]

    role = models.CharField(max_length=20, choices=USER_ROLES)  # Defines user type
    company_name = models.CharField(max_length=255, blank=True, null=True)  # Optional company field
    location = models.CharField(max_length=255, blank=True, null=True)  # Location for GIS integration

    def __str__(self):
        return f"{self.username} ({self.role})"
