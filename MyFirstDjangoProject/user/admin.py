from django.contrib import admin

from .models.account import Account
from .models.profile import Profile

# Register your models here.

admin.site.register(Account)

admin.site.register(Profile)