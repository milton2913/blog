from django import template
from ..models import Menu

register = template.Library()

@register.simple_tag
def get_menu(slug):
    try:
        menu = Menu.objects.prefetch_related('items__children').get(slug=slug)
        # Return only top level items, children will be handled in template
        return menu.items.filter(parent__isnull=True).order_by('order')
    except Menu.DoesNotExist:
        return []
