from django.db import models
from django.utils import timezone


class Poll(models.Model):
    # should it be allowed to create a poll without any name?

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.name} {self.start_date} {self.end_date}'
