from django import template
import django
from django.http import QueryDict


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'real_estate.settings')
django.setup()

register = template.Library()


@register.simple_tag
def make_query_dict(dictionary):
    query_dict = QueryDict('', mutable=True)
    query_dict.update(dict(dictionary))
    return query_dict
    


q = make_query_dict({'id': 1, 'title': 'Nice house down the hill', 'price': 3000, 'num_bedrooms': 2,
                     'num_bathrooms': 2, 'sq_footage': 400, 'address': '12/23/234', 'image': 'property-g996a44ad7_640.jpg'})


print(q)
