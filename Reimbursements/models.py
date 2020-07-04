from django.db import models
from Accounts.models import User
from uuid import uuid4
import uuid

# Create your models here.
class Bill(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='bill')
    name = models.CharField(max_length = 100)
    bill = models.ImageField()
    remarks = models.TextField(null = True)

    NOT_REVIEWED = 'Not Reviewed'
    PAID = 'Paid'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (NOT_REVIEWED, 'Not Reviewed'),
        (PAID, 'Paid'),
        (REJECTED, 'Rejected')
    ]
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = NOT_REVIEWED
    )

    comments = models.CharField(max_length=200, default = '-')