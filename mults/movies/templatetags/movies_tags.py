from django import template

from movies.models import Tags
from django.db.models import Count

register = template.Library()


@register.simple_tag
def get_tags():
    return Tags.objects.all()


@register.inclusion_tag('movies/list_tags.html')
def show_tags():
    tags = Tags.objects.annotate(cnt=Count('movies')).filter(cnt__gt=0)
    return {'tags': tags}
