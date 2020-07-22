from django.db import models
import uuid
from uuid import uuid4
# Create your models here.
class Project(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key = True)
    name = models.CharField(max_length = 100, default = 'NAME')
    description = models.TextField(null = True)
    mentor = models.CharField(max_length = 100)

    member1 = models.CharField(max_length = 100)
    member2 = models.CharField(max_length = 100, blank = True, default = "")
    member3 = models.CharField(max_length = 100, blank = True, default = "")
    member4 = models.CharField(max_length = 100, blank = True, default = "")
    member5 = models.CharField(max_length = 100, blank = True, default = "")
    member6 = models.CharField(max_length = 100, blank = True, default = "")