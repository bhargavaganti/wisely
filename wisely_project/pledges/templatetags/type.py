from django import template
from django.contrib.contenttypes.models import ContentType

from pledges.models import Pledge


register = template.Library()


@register.filter('pledgeType')
def pledgeType(obj):
    if not obj:
        return False
    return ContentType.objects.get_for_model(obj) is Pledge