import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from user.pagination import StandardResultsPagination
from user.models import Profile
from user.serializer.profile_serializer import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = StandardResultsPagination



    def retrieve(self, request, pk=None):
        profile = Profile.objects.filter(pk=pk).first()
        if not profile:
            return Response({
                "message"   : "Profile not found.",
                "status"    : 0,
                "data"      : None
            })
        
        serializer = self.get_serializer(profile)
        return Response({
            "message"   : "Profile",
            "status"    : 1,
            "data"      : serializer.data
        })
    


    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "message"   : "New profile created.",
            "status"    : 1,
            "data"      : serializer.data
        })

        return Response({
            "message"   : "New profile NOT created.",
            "status"    : 0,
            "data"      : serializer.errors
        })
    


    def update(self, request, pk):
        profile = Profile.objects.filter(pk=pk).first()

        if not profile:
            return Response({
                "message"   : "Profile not found.",
                "status"    : 0,
                "data"      : None
            })


        serializer = self.get_serializer(profile, data=request.data)
        # serializer = self.get_serializer(data=request.data)


        if serializer.is_valid():
            # data = serializer.data
            # profile.first_name = data.first_name 
            # profile.last_name = data.last_name            
            # profile.phone_number = data.phone_number            
            # profile.date_of_birth = data.date_of_birth
            # profile.account = data.account
            # profile.save()

            serializer.save()
            return Response({
            "message"   : "Profile updated.",
            "status"    : 1,
            "data"      : serializer.data
            })
        return Response({
            "message"   : "Profile NOT updated.",
            "status"    : 0,
            "data"      : serializer.errors
        })
    


    def destroy(self, request, pk):
        profile = Profile.objects.filter(pk=pk).first()

        if not profile:
            return Response({
                "message"   : "Profile not found.",
                "status"    : 0,
                "data"      : None
            })
        
        profile.delete()

        return Response({
            "message"   : "Profile deleted.",
            "status"    : 1,
            "data"      : None
            })
                


    @action(detail=False, methods=["get"])         
    def all(self, request):
    
        recent_profiles = Profile.objects.all().order_by("-account")
        page = self.paginate_queryset(recent_profiles)   
    
        if page is not None:
            serializer = self.get_serializer(page, many=True)    
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(recent_profiles, many=True)
        return Response(serializer.data)
    
    
    
    @action(detail=False)
    def test_registered_phone_number(self, request):

        phone_number = request.GET.get('phone_number')
        is_registered = Profile.objects.filter(phone_number=phone_number).exists()

        if is_registered:
            return Response({
                "message": "The phone number is registered under a profile"
            })

        return Response({
            "message": "The phone number is not registered under any profile"
        })
