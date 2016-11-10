from datetime import date
from testapp.config import AGE, BIZZ_VALUE, FUZZ_VALUE

def eligible(birthday):
	current = date.today()
	age = current.year - birthday.year - ((current.month, current.day) < (birthday.month, birthday.day))
	return age >= AGE

def bizzfuzz(value):
	if not (value % BIZZ_VALUE or value % FUZZ_VALUE): return 'BizzFuzz'
	elif not (value % BIZZ_VALUE): return 'Bizz'
	elif not (value % FUZZ_VALUE): return 'Fuzz'
	return value
