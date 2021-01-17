from django.shortcuts import render
from django.conf import settings
import jwt, requests
from .models import User
from Members.models import Members
from Members.models import Members
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework import permissions, generics
from .serializers import UserLoginSerializer, UserRegistrationSerializer, ChangePasswordSerializer

# Create your views here.

class UserRegistration(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):

        regno = request.data['regno']
        try:
            category = Members.objects.get(regno = regno).category
        except:
            return Response('Invalid Registration Number Entered', status = 403)
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response({"email" : serializer.data["email"],"token" : serializer.data["token"], "category" : category}, status=status.HTTP_201_CREATED)

        except:
            return Response({"error" : "Username already exists"}, status = 403)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        regno = User.objects.get(email = email).regno
        category = Members.objects.get(regno = regno).category
        return Response({"email" : serializer.data["email"],"token" : serializer.data["token"], "category" : category}, status=status.HTTP_200_OK)

class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)