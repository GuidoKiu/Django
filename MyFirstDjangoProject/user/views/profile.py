from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from user.models import Profile
from user.serializer.profile_serializer import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=False)
    def recent_profiles(self, request):
        recent_profiles = Profile.objects.all().order_by("-account")   
        serializer = self.get_serializer(recent_profiles, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def test_existing_phone_number(self, request):
        phone_number = request.GET.get('phone_number')
        test = Profile.objects.filter(phone_number=phone_number).exists()
        return Response({
            "result": test
        })