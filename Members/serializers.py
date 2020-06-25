from rest_framework import serializers
from .models import MembersListFile

class MembersListFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembersListFile
        fields = '__all__'
        read_only_fields = ('owner',)