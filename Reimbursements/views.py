from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import BillSerializers
from .models import Bill

# Create your views here.
class BillViewsets(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BillSerializers

    def get_queryset(self):
        myBill = Bill.objects.filter(owner = self.request.user)
        return (myBill)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)