from rest_framework import viewsets
from user.models import Account
from user.serializer import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    # crud
