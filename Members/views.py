from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.decorators import parser_classes
from .serializers import MembersListFileSerializer, MembersSerializer
from .models import MembersListFile, Members
from Profile.models import MyProfile
from django.conf import settings
import pandas as pd
import os


# Create your views here.

@parser_classes((MultiPartParser, JSONParser))
class ListUploadViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MembersListFileSerializer

    def get_queryset(self):
        return self.request.user.member_list.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MembersView(APIView):

    permission_classes = [permissions.IsAuthenticated]


    def post(self, request):
        path = request.data['path']

        # Fetching the required path
        l = len(path)
        count = 0
        for i in range (l):
            if (path[i]=='/'):
                count+=1
            if (count == 4):
                break
        path = path[i+1:]
        csv_file = os.path.join(settings.MEDIA_ROOT, path)

        try:
            df = pd.read_excel(csv_file, sheet_name = 'Sheet1')
        except:
            return Response({"Wrong File Type Uploaded"}, status = 404)
        print (len(df))
        for i in range (len(df)):
            try :
                Members.objects.update_or_create(
                owner = self.request.user,
                regno = df.loc[i, 'REGNO'],
                category = int(df.loc[i, 'CATEGORY'])
                )


            except:
                continue

        csvs = MembersListFile.objects.all()
        if (len(csvs)==0):
            return Response({"Excel does not exist"},status =201)
        for csv in csvs:
            csv.delete()
        return Response({"Success":"Members Updated"},status =201)

class MembersListViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MembersSerializer

    def get_queryset(self):
        members = Members.objects.all()
        return (members)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

    def perform_destroy(self, instance):
        instance.delete()

class MemberNamesList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        members = Members.objects.all()
        members_list = []
        for member in members:
            regno = member.regno
            name = ""
            profile = MyProfile.objects.filter(regno = regno)
            if (not profile.exists()):
                name = "Profile does not exist"
            else:
                name = profile.values('name')[0]
            category = member.category
            member_dict = {
                "name" : name,
                "regno" : regno,
                "category" : category
            }
            members_list.append(member_dict)
        
        return Response({"members" : members_list}, status = 200)
            
    
