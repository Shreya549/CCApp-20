from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        field = '__all__'