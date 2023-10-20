from rest_framework import viewsets
from rest_framework.decorators import action
from user.models import Account
from user.serializer import AccountSerializer, ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    # queryset = Profile.objects.all()
    # serializer_class = ProfileSerializer
    # pagination_class = StandardResultsPagination

    @action(detail=False, methods=["post"])
    def add_new_user(self, request):
        serializer = AccountSerializer(data=request.data.account)
        if serializer.is_valid():
            data = serializer.data
            new_account = Account({
                    "email" : data.email,
                    "username" : data.username,
                    "password" : data.password
                })
            new_account.save()

