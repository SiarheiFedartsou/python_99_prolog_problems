import fractions
import math

# 1
def is_prime(n):
	'''
	>>> is_prime(7)
	True
	>>> is_prime(149)
	True
	>>> is_prime(99999)
	False
	'''
	return [x for x in xrange(2, int(math.sqrt(n)) + 1) if n % x == 0] == []

# 5
def goldbach(n):
	'''
	>>> goldbach(28)
	[(5, 23), (11, 17)]
	>>> goldbach(90)
	[(17, 73), (29, 61), (23, 67), (19, 71), (31, 59), (7, 83), (37, 53), (43, 47), (11, 79), (1, 89)]
	'''
	return list(set([tuple(sorted((x, n - x))) for x in xrange(n) if is_prime(x) and is_prime(n - x)]))

# 6
def goldbach_list(a, b):
	'''
	>>> goldbach_list(9, 20)
	[(10, [(3, 7), (5, 5)]), (12, [(1, 11), (5, 7)]), (14, [(1, 13), (3, 11), (7, 7)]), (16, [(5, 11), (3, 13)]), (18, [(7, 11), (1, 17), (5, 13)])]
	'''
	return [(x, goldbach(x)) for x in xrange(a, b) if x % 2 == 0]

# 7
def gcd(a, b):
	'''
	>>> gcd(36, 63)
	9
	'''
	return fractions.gcd(a, b)


# 8
def coprime(a, b):
	'''
	>>> coprime(35, 64)
	True
	>>> coprime(25, 5)
	False
	'''
	return fractions.gcd(a, b) == 1
	
import doctest
doctest.testmod()