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
from .serializers import UserLoginSerializer, UserRegistrationSerializer

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
