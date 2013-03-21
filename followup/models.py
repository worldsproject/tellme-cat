from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
    link = models.URLField()
    domain = models.URLField()
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)

class FollowUp(models.Model):
    link = models.URLField()
    domain = models.URLField()
    story = models.ForeignKey(Story)
    title = models.CharField(max_length=200)
    time = models.TimeField(auto_now=True)
    is_paid = models.BooleanField()
