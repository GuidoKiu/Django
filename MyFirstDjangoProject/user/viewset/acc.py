import json

from rest_framework import viewsets
from rest_framework.response import Response

from user.models import Account
from user.models import Profile
from user.serializer import AccountSerializerOut, AccountSerializer


class AccViewSet(viewsets.ViewSet):
    def get_accounts(self, request, pk=None):
        accounts = Account.objects.all()
        if not accounts:
            message = "There is no account"
            return Response({"message": message, "status": 1, "data": None})

        message = "Account"
        obj = AccountSerializerOut(accounts, many=True)
        return Response({"message": message, "status": 1, "data": obj.data})

    def get_account(self, request, pk=None):
        account = Account.objects.filter(pk=pk).first()
        if not account:
            message = "Account Not Found"
            return Response({"message": message, "status": 0, "data": None})

        message = "Account Info"
        obj = AccountSerializerOut(account)
        return Response({"message": message, "status": 1, "data": obj.data})

    def add_account(self, request):
        data = request.data
        serializer = AccountSerializer(data=data)

        if serializer.is_valid():
            instance = serializer.save()
            serializer_out = AccountSerializerOut(instance)
            message = "Account Created Successfully"
            return Response({"message": message, "status": 1, "data": serializer_out.data})

        message = "Account Created Failed"
        return Response({"message": message, "status": 0, "data": serializer.errors})

    def update_account(self, request):
        data = request.data

        account = Account.objects.filter(pk=data['id']).first()
        if not account:
            message = "Account Not Found"
            return Response({"message": message, "status": 0, "data": None})

        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            account.username = serializer.data['username']
            account.email = serializer.data['email']
            account.password = serializer.data['password']
            account.save()

            serializer_out = AccountSerializerOut(account)
            message = "Account update successfully"
            return Response({"message": message, "status": 1, "data": serializer_out.data})

        message = "Account update failed"
        return Response({"message": message, "status": 0, "data": serializer.errors})

    def delete_account(self, request, pk):
        account = Account.objects.filter(pk=pk).first()
        if not account:
            message = "Account Not Found"
            return Response({"message": message, "status": 0})

        account.delete()
        message = "Account deleted successfully"
        return Response({"message": message, "status": 1})
