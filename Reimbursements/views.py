from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import BillSerializers
from .models import Bill
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser

# Create your views here.
@parser_classes((MultiPartParser, JSONParser))
class BillViewsets(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BillSerializers

    def get_queryset(self):
        myBill = Bill.objects.filter(owner = self.request.user)
        return (myBill)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user, name = self.request.user.name)