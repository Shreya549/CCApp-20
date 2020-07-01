from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingViewSet

router = DefaultRouter()
router.register('new', MeetingViewSet, basename = 'new')
urlpatterns = router.urls