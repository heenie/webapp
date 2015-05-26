from django import template
register = template.Library()


@register.filter(name='add')
def add(value, arg):
    try:
        value = int(value)
        arg = int(arg)
        return value + arg
    except:
        pass
    return ''


@register.filter(name='sub')
def sub(value, arg):
    try:
        value = int(value)
        arg = int(arg)
        return value - arg
    except:
        pass
    return ''


@register.filter(name='integer')
def integer(value):
    return int(value)


@register.filter("truncate_chars")
def truncate_chars(value, max_length):
    if len(value) > max_length:
        truncd_val = value[:max_length]
        if not len(value) == max_length+1 and value[max_length+1] != " ":
            truncd_val = truncd_val[:truncd_val.rfind(" ")]
        return  truncd_val + "..."
    return value