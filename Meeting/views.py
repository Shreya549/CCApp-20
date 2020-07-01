from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import MeetingSerializer
from .models import Meeting
from Members.models import Members

# Create your views here.
class MeetingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MeetingSerializer

    def get_queryset(self):
        meetings = Meeting.objects.all()
        return (meetings)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        print(Members.objects.filter(regno = (self.request.user.regno)).values('category'))
        serializer.save(owner=self.request.user)