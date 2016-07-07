from django import template
from lmhsweb import models

register = template.Library()


@register.assignment_tag
def types():
    type_list = []
    for t in models.TYPE_CHOICES:
        for tt in t:
            type_list.append(tt)
            break
    return type_list
