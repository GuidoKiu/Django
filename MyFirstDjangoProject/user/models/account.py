from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__ (self):
        return self.username