from django.db import models
from django.contrib.auth.models import AbstractUser
from master.models import Address,TimeStamp
from django.utils import timezone

# Create your models here.


class CustomUser(AbstractUser):
    pass


class Profile(TimeStamp,models.Model):
    GENDER_CHOICES = (
        ("m", "Male"),
        ("f", "Female"),
        ("t", "Transgender"),
    )
    name = models.CharField(max_length=52)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.CharField(max_length=5)
    qualification = models.CharField(max_length=50)
    dob = models.DateField(default=timezone.now)
    phone = models.CharField(max_length=10)
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True
    )
    def __str__(self) -> str:
        return f"{self.name}"