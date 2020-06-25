from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListUploadViewSet, MembersView, MembersListViewSet

router = DefaultRouter()
router.register('upload', ListUploadViewSet, basename = 'upload')
router.register('view', MembersListViewSet, basename = 'view')
urlpatterns = router.urls

urlpatterns += [
    path('register/', MembersView.as_view())
]

