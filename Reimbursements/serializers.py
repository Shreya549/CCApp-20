from rest_framework import serializers
from .models import Bill

class BillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
        read_only_fields = ('owner')