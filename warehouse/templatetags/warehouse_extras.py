from django import template

from warehouse import models

register = template.Library()


@register.filter
def uah(value):
    return f"{value} грн"


@register.simple_tag
def product_count():
    return models.Sports_equipment.objects.count()
