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