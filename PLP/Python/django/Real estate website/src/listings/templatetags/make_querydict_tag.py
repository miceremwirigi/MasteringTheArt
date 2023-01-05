from django import template
import django
from django.http import QueryDict


# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE',
#                       'real_estate.settings')
# django.setup()

register = template.Library()


@register.filter
def make_query_dict(name, dictionary):
    query_dict = QueryDict('', mutable=True)
    query_dict.update(dict(dictionary))
    return query_dict
