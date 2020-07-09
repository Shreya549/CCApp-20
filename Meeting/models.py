from django.db import models
from Accounts.models import User
from uuid import uuid4
import uuid

# Create your models here.
class Meeting(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='meeting')
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length = 100)
    time = models.TimeField()
    date = models.DateField()
    description = models.TextField()
    members = models.CharField(max_length = 200, default = 'All Core Committee Members')
    latitude = models.CharField(max_length = 100, null = True)
    longitude = models.CharField(max_length = 100, null = True)
    start_time = models.DateTimeField(null = True)



