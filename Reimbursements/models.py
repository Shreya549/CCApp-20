from django.db import models
from Accounts.models import User
from uuid import uuid4
import uuid, os

# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'bills'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Bill(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='bill')
    name = models.CharField(max_length = 100, null = True)
    bill = models.ImageField(upload_to = path_and_rename, null = True, blank = True)

    remarks = models.TextField(null = True) # By person who will be paid

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

    comments = models.CharField(max_length=200, default = '-') # By Finance Director