from datetime import datetime

from django import template

from materials.models import Material

register = template.Library()


@register.simple_tag()
def get_available_materials():
    current_time = datetime.now()
    return Material.objects.filter(start_time__gt=current_time)
