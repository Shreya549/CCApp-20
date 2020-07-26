from django.urls import path, include
from .views import BillViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('new', BillViewsets, basename = 'new')
urlpatterns = router.urls