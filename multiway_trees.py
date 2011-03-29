import types

# 1
def is_tree(tree):
	'''
	>>> is_tree(('a', [('b', []), ('c', [('b', [])])]))
	True
	>>> is_tree(([],))
	True
	>>> is_tree(('a', [('b', [])], 'c'))
	False
	>>> is_tree(('a',))
	False
	'''
	if  type(tree) is types.TupleType and not len(tree) == 2: return tree == ([],)
	for subtree in tree:
		if type(subtree) is types.TupleType or type(subtree) is types.ListType: return is_tree(subtree) 
	return True



import doctest
doctest.testmod()