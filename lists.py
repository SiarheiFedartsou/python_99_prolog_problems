import types


def last_list_element(l):
	'''
	>>> last_list_element([1, 2, 3])
	3
	'''
	return l[-1]
	
def last_but_one_list_element(l):
	'''
	>>> last_but_one_list_element([1, 2, 3])
	2
	'''
	return l[-2]
	
def element_at(l, k):
	'''
	>>> element_at([1, 2, 3, 4, 5], 3)
	4
	'''
	return l[k];
		
def number_of_list_elements(l):
	'''
	>>> number_of_list_elements([])
	0
	>>> number_of_list_elements([1, 2, 3])
	3
	'''
	return len(l)
	
#def reversed_list(l):
#	'''
#	>>> reversed_list([1, 2, 3])
#	[3, 2, 1]
#	'''	
#	return l.reverse()

def is_palindrome(l):
	'''
	>>> is_palindrome([1, 2, 2, 3, 2, 2, 1])  
	True
	>>> is_palindrome([1, 4, 2, 3, 2, 2, 1])  
	False
	'''
	for i in xrange(len(l) / 2 + 1):
		if l[i] != l[len(l) - i - 1]:
			return False
	return True

def flat_list_structure(l):
	'''
	>>> flat_list_structure([[1, [2, [3]], 3], 5])
	[1, 2, 3, 3, 5]
	'''
	result = []
	for x in l:
		if type(x) is types.ListType:
			result.extend(flat_list_structure(x))
		else:
			result.append(x)
	return result
	

import doctest
doctest.testmod()