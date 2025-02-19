from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('project', 'Project User'),
        ('supplier', 'Supplier User'),
        ('bouwhub', 'Bouwhub User'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=USER_ROLES, default='project')

    def __str__(self):
        return f"{self.username} - {self.role}"
