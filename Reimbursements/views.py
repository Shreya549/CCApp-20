from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import BillSerializers
from .models import Bill
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
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

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

    def perform_destroy(self, instance):
        instance.delete()

class ViewBillViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = BillSerializers

    def get_queryset(self):
        bill = Bill.objects.all()
        return (bill)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

    def perform_destroy(self, instance):
        instance.delete()
