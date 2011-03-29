import operator

# 1 
def truth_table(func):
	'''
	>>> truth_table(lambda a, b: operator.__and__(a, operator.__or__(a, b)))	
	[(True, True, True), (True, False, True), (False, True, False), (False, False, False)]
	'''
	return [(a, b, func(a, b)) for a in (True, False) for b in (True, False)]
	
	
# 2
def truth_table_2(func):
	'''
	>>> truth_table_2(lambda a, b: a and (a or not b))	
	[(True, True, True), (True, False, True), (False, True, False), (False, False, False)]
	'''
	return [(a, b, func(a, b)) for a in (True, False) for b in (True, False)]


import doctest
doctest.testmod()	