from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyProfileViewSet, ViewAllProfileViewSet

router = DefaultRouter()
router.register('profile', MyProfileViewSet, basename = 'myProfile'),
router.register('allProfile', ViewAllProfileViewSet, basename = 'allProfile')
urlpatterns = router.urls
