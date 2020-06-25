from rest_framework import serializers
from .models import MyProfile

class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProfile
        fields = '__all__'
        read_only_fields = ('owner',)

