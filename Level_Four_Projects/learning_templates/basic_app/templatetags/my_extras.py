from django import template

register = template.Library()

@register.filter(name='cutitout')
def cutitout(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('cutitout', cutitout)
