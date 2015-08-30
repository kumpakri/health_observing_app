#app_filters.py
from django import template

register = template.Library()

@register.filter(name='get_at_index')
def get_at_index(list, index):
    return list[index]

@register.filter(name='get_length_of_values_span')
def get_length_of_values_span(dict, key):
	if len(dict[key])>0:
		ret= len(dict[key])
	else:
		ret=1
	return  ret

@register.filter(name='get_length_of_values')
def get_length_of_values(dicty, key):
	return  len(dicty[key])

@register.filter(name='get_time')
def get_time(entry):
	return entry.datetime.time().strftime('%H:%M')

@register.filter(name='get_value')
def get_value(entry):
	return entry.value

@register.filter(name="get_range")
def get_range(num):
	return range(1,num)
	