from django.urls import path, include
from .views import BillViewsets, ViewBillViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('new', BillViewsets, basename = 'new')
router.register('view', ViewBillViewSet, basename = 'view')
urlpatterns = router.urls