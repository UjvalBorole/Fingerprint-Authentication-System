from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["userlog", "pic"]


@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    list_display = ["email", "password"]
