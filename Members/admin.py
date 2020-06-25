from django.contrib import admin
from .models import MembersListFile, Members

# Register your models here.
admin.site.register(MembersListFile)
admin.site.register(Members)