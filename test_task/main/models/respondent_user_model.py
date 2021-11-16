from django.contrib.auth.models import User
from django.db import models


class RespondentUser(models.Model):
    id = models.AutoField(primary_key=True)
    authorized_credentials = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session_cookies = models.CharField(max_length=255, blank=True, null=True)
