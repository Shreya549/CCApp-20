from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingViewSet, MarkAttendanceViewSet, ViewAttendeesViewSet
import uuid

router = DefaultRouter()
router.register('new', MeetingViewSet, basename = 'new')
router.register('mark', MarkAttendanceViewSet, basename = 'mark')
urlpatterns = router.urls

