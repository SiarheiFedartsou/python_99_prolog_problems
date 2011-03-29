import types
import random

# 1
def last_list_element(l):
	'''
	>>> last_list_element([1, 2, 3])
	3
	'''
	return l[-1]

# 2	
def last_but_one_list_element(l):
	'''
	>>> last_but_one_list_element([1, 2, 3])
	2
	'''
	return l[-2]

# 3	
def element_at(l, k):
	'''
	>>> element_at([1, 2, 3, 4, 5], 3)
	4
	'''
	return l[k]

# 4		
def number_of_list_elements(l):
	'''
	>>> number_of_list_elements([])
	0
	>>> number_of_list_elements([1, 2, 3])
	3
	'''
	return len(l)

# 5
def reversed_list(l):
	'''
	>>> reversed_list([1, 2, 3])
	[3, 2, 1]
	'''	
	return list(reversed(l))

# 6
def is_palindrome(l):
	'''
	>>> is_palindrome([1, 2, 2, 3, 2, 2, 1])  
	True
	>>> is_palindrome([1, 4, 2, 3, 2, 2, 1])  
	False
	'''
	return l == reversed_list(l)

# 7
def flat_list_structure(l):
	'''
	>>> flat_list_structure([[1, [2, [3]], 3], 5])
	[1, 2, 3, 3, 5]
	'''
	result = []
	for x in l: 
		if type(x) is types.ListType: result.extend(flat_list_structure(x)) 
		else: result.append(x)
	return result

# 8
def compress_list(l):
	'''
	>>> compress_list([1, 1, 1, 1, 2, 2, 2, 3, 7, 3, 3, 2, 2, 5, 5, 6])
	[1, 2, 3, 7, 3, 2, 5, 6]
	'''
	return [x for i, x in enumerate(l[:-1]) if not l[i] == l[i + 1]] + [l[-1]]
	#return list(set(l))

# 8
def pack_list(l):
	'''
	>>> pack_list([1, 1, 1, 1, 2, 2, 2, 3, 7, 3, 3, 2, 2, 5, 5, 6])
	[[1, 1, 1, 1], [2, 2, 2], [3], [7], [3, 3], [2, 2], [5, 5], [6]]
	'''
	result = []
	t = []
	for i, x in enumerate(l[:-1]):
		t.append(x)
		if not l[i] == l[i+1]: 
			result.append(t)
			t = []
	return result
	#return list(set(l))
# 14
def dupl_list(l):
	'''
	>>> dupl_list(['a', 'b', 'c', 'c', 'd'])
	['a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd']
	'''
	return list(sorted(l * 2))

# 15
def dupl_list_n(l, n):
	'''
	>>> dupl_list_n(['a', 'b', 'c'], 3)
	['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
	'''
	return list(sorted(l * n))

# 16
def drop_every_n(l, n):
	'''
	>>> drop_every_n(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k'], 3)
	['a', 'b', 'd', 'e', 'g', 'h', 'k']
	'''
	return [x for i, x in enumerate(l) if not (i + 1) % n == 0]
# 17
def split(l, n):
	'''
	>>> split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k'], 3)
	(['a', 'b', 'c'], ['d', 'e', 'f', 'g', 'h', 'i', 'k'])
	'''
	return (l[:n], l[n:])
	
# 18 
def slice(l, a, b):
	'''
	>>> slice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k'], 3, 7)
	['c', 'd', 'e', 'f', 'g']
	'''
	return l[a-1:b]
	
# 19 
def rotate(l, n):
	'''
	>>> rotate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 3)
	['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
	>>> rotate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], -2)
	['g', 'h', 'a', 'b', 'c', 'd', 'e', 'f']
	'''
	return l[n:] + l[:n]
	
# 22
def create_range(a, b):
	'''
	>>> create_range(4, 9)
	[4, 5, 6, 7, 8, 9]
	'''
	return range(a, b + 1)

# 23
def random_select(l, n):
	'''
	it is not good idea :)
	'''
	return [random.choice(l) for x in xrange(n)]
	
# 25 
def random_permutation(l):
	'''
	it is not good idea :)
	'''
	random.shuffle(l)
	return l

# 28a
def length_sort(l):
	'''
	>>> length_sort([['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['d', 'e'], ['i', 'j', 'k', 'l'], ['m', 'n'], ['o']])
	[['o'], ['d', 'e'], ['d', 'e'], ['m', 'n'], ['a', 'b', 'c'], ['f', 'g', 'h'], ['i', 'j', 'k', 'l']]
	'''
	return list(sorted(l, key = len))
	
# 28b
def freq_length_sort(l):
	'''
	>>> freq_length_sort([['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['d', 'e'], ['i', 'j', 'k', 'l'], ['m', 'n'], ['o']])
	[['i', 'j', 'k', 'l'], ['o'], ['a', 'b', 'c'], ['f', 'g', 'h'], ['d', 'e'], ['d', 'e'], ['m', 'n']]
	'''
	return list(sorted(l, key = lambda x: map(len, l).count(len(x))))

import doctest
doctest.testmod()