from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserLogin, UserRegistration

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view()),
    path('register/', UserRegistration.as_view()),
    path('login/', UserLogin.as_view()),

]