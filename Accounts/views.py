from django.shortcuts import render
from django.conf import settings
import jwt, requests, uuid, os, environ
from uuid import uuid4
from .models import User, OTPStore
from rest_framework.generics import UpdateAPIView
from Members.models import Members
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework import permissions, generics
from .serializers import UserLoginSerializer, UserRegistrationSerializer, ChangePasswordSerializer
from datetime import datetime, timezone
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env()
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CC20App.settings.local")

SENDGRID_API_KEY = env('SENDGRID_API_KEY')
# Create your views here.

class UserRegistration(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):

        regno = request.data['regno']
        fcm = request.data['fcm']
        try:
            category = Members.objects.get(regno = regno).category
        except:
            return Response('Invalid Registration Number Entered', status = 403)
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception = True)
            serializer.save()

            member = Members.objects.get(regno = regno)
            member.fcm = fcm
            member.save()

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

class OTPView(APIView):
    def post(self, request):
        email = request.data['email']
        user = User.objects.filter(email = email)
        if (user.exists()):
            code =  (str(uuid.uuid4()))[:8]
            otp = OTPStore.objects.create(
                email = email,
                otp = code,
                timestamp = datetime.now(timezone.utc)
            )
            otp.save()
            subject = 'Password reset OTP'
            message = "OTP - " + code + "<br>"
            msg = message
            message = Mail(
                from_email='codechefvit@gmail.com',
                to_emails=email,
                subject=subject,
                html_content=msg)
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            return Response(status = response.status_code)
        else:
            return Response({'message' : "Email does not exist"}, status = 400)

class OTPCheckView(APIView):
    def post(self, request):
        email = request.data['email'] 
        otp = request.data['otp']
        password = request.data['password']
        query = OTPStore.objects.filter(email = email, otp = otp).order_by('-timestamp')
        if (query.exists()):
            timestamp = query.values_list('timestamp', flat=True)[0]
            duration = datetime.now(timezone.utc) - timestamp
            duration_in_s = duration.total_seconds()
            minutes = divmod(duration_in_s, 60)[0]
            if (minutes<=5):
                user = User.objects.get(email = email)
                user.set_password(password)
                user.save()
                return Response({'message' : 'Password changed successfully'}, status = 200)
            else:
                return Response({"message" : "Time Out"}, status = 400)
        else:
            return Response({"message" : "Invalid details entered"}, status = 404)