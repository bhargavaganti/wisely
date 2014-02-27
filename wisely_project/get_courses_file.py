import sys
import os
import traceback

from django import db


sys.path.append('/root/wisely/wisely_project/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'wisely_project.settings.production'

from django.db.models import F
from django.utils import timezone
from users.tasks import get_coursera_courses, get_edx_courses

__author__ = 'tmehta'

from users.models import CourseraProfile, EdxProfile

while True:
    try:
        db.reset_queries()
        for user in CourseraProfile.objects.filter(last_updated__lt=F('user__last_login')):
            get_coursera_courses(user)
            user.last_updated = timezone.now()
            user.save()
        for user in EdxProfile.objects.filter(last_updated__lt=F('user__last_login')):
            get_edx_courses(user)
            user.last_updated = timezone.now()
            user.save()
    except Exception as e:
        print traceback.format_exc()
