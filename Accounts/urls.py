from django.urls import path, include
from .views import UserLogin, UserRegistration, ChangePasswordView, OTPCheckView, OTPView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('register/', UserRegistration.as_view()),
    path('login/', UserLogin.as_view()),
    path('changePassword', ChangePasswordView.as_view()),
    path('resetPassword', OTPView.as_view()),
    path('checkOTP', OTPCheckView.as_view()),
]