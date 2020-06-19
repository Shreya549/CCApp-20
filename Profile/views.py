from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import MyProfileSerializer
from .models import MyProfile


# Create your views here.
class MyProfileViewSet(viewsets.ModelViewSet):

    serializer_class = MyProfileSerializer

    def get_queryset(self):
        return self.request.user.myProfile.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
