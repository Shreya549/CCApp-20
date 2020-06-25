from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListUploadViewSet

router = DefaultRouter()
router.register('upload', ListUploadViewSet, basename = 'upload')
urlpatterns = router.urls
