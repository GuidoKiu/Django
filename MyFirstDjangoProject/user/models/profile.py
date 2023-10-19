from django.db import models

from .account import Account


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False
    )
