import itertools
import types

# 4
def arith_puzzle(l):
	'''
	>>> arith_puzzle([2, 3, 5, 7, 11])
	['2-3+5+7==11', '2-3+5+7==11', '2+3==5+7/11', '2+3==5+7/11', '2==3-5-7+11', '2==3-5-7+11', '2+3-5==7/11', '2+3==5-7/11', '2/3/5==7/11', '2/3/5==7/11', '2/3==5/7/11', '2/3==5/7/11', '2/3/5==7/11', '2/3/5==7/11', '2/3==5/7/11', '2/3==5/7/11', '2/3/5==7/11', '2/3/5==7/11', '2/3==5/7/11', '2/3==5/7/11', '2/3*5==7/11', '2/3==5/7*11', '2/3*5==7/11', '2/3==5/7*11']
	'''
	result = []
	for operator_list in itertools.combinations_with_replacement(['+', '-', '/', '*', '=='], len(l) - 1):
		for operator_list_permutation in itertools.permutations(operator_list):
			expr = str(l[0])
			for i, operand in enumerate(map(str, l[1:])):
				expr += operator_list_permutation[i]
				expr += operand
			try:
				eval_result = eval(expr)
				if type(eval_result) is types.BooleanType and eval_result == True:
					result.append(expr)
			except: pass
	return result

# 5 
def english_number_words(n):
	'''
	>>> english_number_words(175)
	'one-seven-five'
	>>> english_number_words(0)
	'zero'
	>>> english_number_words(201)
	'two-zero-one'
	'''
#	number_words = 
	return '-'.join(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'][number_words[int(c)] for c in str(n)])

import doctest
doctest.testmod()