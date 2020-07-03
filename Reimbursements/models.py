from django.db import models
from Accounts.models import User
from uuid import uuid4

# Create your models here.
class Bill(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='member_list')
    name = models.CharField(max_length = 100)
    bill = models.ImageField()
    remarks = models.TextField()
    status = models.CharField(max_length = 200)