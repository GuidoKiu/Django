from rest_framework import serializers
from user.models import Account


class AccountSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email', 'password')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
