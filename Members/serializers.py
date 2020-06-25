from rest_framework import serializers
from .models import MembersListFile, Members

class MembersListFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembersListFile
        fields = '__all__'
        read_only_fields = ('owner',)

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'
        read_only_fields = ('owner',)