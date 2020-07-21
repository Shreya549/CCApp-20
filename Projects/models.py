from django.db import models
import uuid
from uuid import uuid4
# Create your models here.
class Project(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key = True)
    mentor = models.CharField(max_length = 100)

    member1 = models.CharField(max_length = 100)
    regno1 = models.CharField(max_length = 9)

    member2 = models.CharField(max_length = 100, null = True)
    regno2 = models.CharField(max_length = 9, null = True)

    member3 = models.CharField(max_length = 100, null = True)
    regno3 = models.CharField(max_length = 9, null = True)

    member4 = models.CharField(max_length = 100, null = True)
    regno4 = models.CharField(max_length = 9, null = True)

    member5 = models.CharField(max_length = 100, null = True)
    regno5 = models.CharField(max_length = 9, null = True)
    
    member6 = models.CharField(max_length = 100, null = True)
    regno6 = models.CharField(max_length = 9, null = True)