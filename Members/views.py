from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.decorators import parser_classes
from .serializers import MembersListFileSerializer
from .models import MembersListFile

# Create your views here.

@parser_classes((MultiPartParser, JSONParser))
class ListUploadViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MembersListFileSerializer

    def get_queryset(self):
        return self.request.user.member_list.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)