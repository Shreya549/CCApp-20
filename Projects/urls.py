from django.urls import path, include
from .views import ProjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('new', ProjectViewSet, basename = 'new')
urlpatterns = router.urls
