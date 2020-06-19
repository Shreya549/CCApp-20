from django.db import models
from uuid import uuid4
from Accounts.models import User
import uuid

# Create your models here.
class MyProfile(models.Model):
    uuid = models.UUIDField(primary_key=True, default = uuid.uuid4)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='myProfile')
    name = models.CharField(max_length = 100)
    regno = models.CharField(max_length = 10, unique = True)
    email = models.EmailField(unique = True)
    phone = models.CharField(unique = True, max_length = 15)

    MALE = 'MAL'
    FEMALE = 'FEM'
    OTHER = 'OTH'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]
    gender = models.CharField(
        max_length = 3,
        choices = GENDER_CHOICES,
        default = OTHER
    )

    room = models.CharField(max_length = 10)
    block = models.CharField(max_length = 20)


