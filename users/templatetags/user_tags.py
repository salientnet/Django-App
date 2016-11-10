from django import template
from users.utils import eligible, bizzfuzz

register = template.Library()

@register.simple_tag
def eligible_tag(birthday):
	return 'allowed' if eligible(birthday) else 'blocked'

@register.simple_tag
def bizzfuzz_tag(value):
	return bizzfuzz(value)
