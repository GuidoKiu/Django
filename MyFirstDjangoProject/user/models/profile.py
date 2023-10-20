from django.db import models

from .account import Account


class Profile(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        blank=False
    )

    def __str__(self):
        if not self.last_name:
            return self.first_name
        return "{} {}".format(self.first_name, self.last_name)
        
