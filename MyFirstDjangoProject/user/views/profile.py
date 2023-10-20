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

    @action(detail=False)
    def recent_profiles(self, request):
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
        isRegistered = Profile.objects.filter(phone_number=phone_number).exists()
        if isRegistered:
            return Response({
                "message": "The phone number is registered under a profile"
            })
        return Response({
            "message": "The phone number is not registered under any profile"
        })