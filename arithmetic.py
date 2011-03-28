import fractions

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