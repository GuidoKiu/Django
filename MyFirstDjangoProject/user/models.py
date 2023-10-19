from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


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
