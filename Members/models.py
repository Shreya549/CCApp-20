from django.db import models
from Accounts.models import User
from uuid import uuid4
import uuid, os

def path_and_rename(instance, filename):
    upload_to = 'members'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

# Create your models here.
class MembersListFile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='member_list')
    csv = models.FileField(upload_to=path_and_rename)
