from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import MeetingSerializer, AttendanceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Meeting, Attendance
from Members.models import Members
from Accounts.models import User

# Create your views here.
class MeetingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MeetingSerializer

    def get_queryset(self):
        meetings = Meeting.objects.all()
        return (meetings)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     category = Members.objects.get(regno = self.request.user.regno).category
    #     if (category == 3 or category == 5):
    #         serializer.save(owner=self.request.user)
    #         members = Members.objects.filter(category__in = [1,2]).values_list("regno", flat = True)
    #         for i in members:
    #             entry = Attendance.objects.create(meeting = serializer.data['uuid'], regno = i)
    #             entry.save()

    def create(self, request, *args, **kwargs):

        category = Members.objects.get(regno = request.user.regno).category
        if (category == 3 or category == 5):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save(owner = self.request.user)
            headers = self.get_success_headers(serializer.data)
            members = Members.objects.filter(category__in = [1,2]).values_list("regno", flat = True)
            for i in members:
                entry = Attendance.objects.create(meeting = serializer.data['uuid'], regno = i)
                entry.save()

            query = Members.objects.filter(category__in = [1,2,3,5]).values_list("regno", "category", "fcm")
            return Response({"members" : query}, status=202)
    
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
        attendance = Attendance.objects.filter(meeting=meeting, regno = regno).values_list('uuid', flat = True)[0]
        print(attendance)
        attn = Attendance.objects.get(uuid=attendance)
        print(attn)
        attn.isPresent = True
        attn.save()
        print(attn)
        return (Attendance.objects.filter(uuid=attendance))


'''class ViewAttendeesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        meeting = self.request.GET.get('meeting')
        return (Attendance.objects.filter(meeting = meeting))'''

class ViewAttendees(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        meeting = self.request.GET.get('meeting')
        attendance = (Attendance.objects.filter(meeting = meeting))
        attendee_list = []
        for attn in attendance:
            uuid = attn.uuid
            regno = attn.regno
            try:
                profile = User.objects.get(regno = regno)
                name = profile.name
            except:
                name = 'Name not found'
            isPresent = attn.isPresent
            attn_dict = {
                "uuid" : uuid,
                "name" : name,
                "regno" : regno,
                "attendance" : isPresent
            }
            attendee_list.append(attn_dict)
        return Response({"attendance" : attendee_list}, status = 200)    