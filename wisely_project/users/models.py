from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Course(models.Model):
    title = models.CharField(max_length=400)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    courses = models.ManyToManyField(Course)
    coursera_username = models.CharField(max_length=100, default="")
    coursera_password = models.CharField(max_length=100, default="")
    last_updated = models.DateTimeField(default=timezone.now())
    announcements = models.CharField(max_length=1000000, default="")