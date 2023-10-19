from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
