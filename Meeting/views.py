from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import MeetingSerializer, AttendanceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Meeting, Attendance
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
        category = Members.objects.get(regno = self.request.user.regno).category
        if (category == 3 or category == 5):
            serializer.save(owner=self.request.user)
            members = Members.objects.filter(category__in = [1,2]).values_list("regno", flat = True)
            for i in members:
                entry = Attendance.objects.create(meeting = serializer.data['uuid'], regno = i)
                entry.save()
        try :
            pass
        except:
            pass
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

    def perform_destroy(self, instance):
        instance.delete()

class MarkAttendanceViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        meeting = self.request.GET.get('meeting')
        regno = self.request.user.regno
        filters = [DjangoFilterBackend]
        attendance = Attendance.objects.filter(meeting=meeting, regno = regno).values_list('uuid', flat = True)[0]
        print("Hello World")
        attn = Attendance.objects.filter(pk=attendance)
        attn.isPresent = True
        attn.save()
        return (attendance)