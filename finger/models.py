from django.db import models


class UserLog(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=15)


class User(models.Model):
    userlog = models.OneToOneField(UserLog, on_delete=models.CASCADE)
    pic = models.CharField(max_length=30)
