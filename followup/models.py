from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
    link = models.URLField()
    domain = models.URLField()
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)

class FollowUp(models.Model):
    user = models.ForeignKey(User)
    link = models.URLField()
    domain = models.URLField()
    story = models.ForeignKey(Story)
    title = models.CharField(max_length=200)
    time = models.TimeField(auto_now=True)
    is_paid = models.BooleanField()

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=30)
    domain_owner = models.BooleanField()
    domain = models.URLField()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

