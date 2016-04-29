def checkio(anything):
	"""
	    try to return anything else :)
	"""
	
	if type(anything) == int:
		if len(str(anything)) == 1:
			return ord
		else:
			return str(anything)
	if type(anything) == type(re):
		if( anything.__name__ == 're'):
			print( "re <= math", re <= math)
			return re
		else:
			return(anything.__name__)
	return anything

if __name__ == '__main__':
	import re
	import math
	assert checkio({}) != [],         'You'
	assert checkio('Hello') < 'World', 'will'
	assert checkio(80) > 81,           'never'
	assert checkio(re) >= re,          'make'
	assert checkio(re) <= math,        'this'
	assert checkio(5) == ord,          ':)'
	print('NO WAY :(')