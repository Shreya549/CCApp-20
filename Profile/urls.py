from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyProfileViewSet

router = DefaultRouter()
router.register('profile', MyProfileViewSet, basename = 'myProfile')
urlpatterns = router.urls
