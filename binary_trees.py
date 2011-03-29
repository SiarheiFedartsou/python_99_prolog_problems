import types

# 1

def is_tree(tree):
	'''
	>>> is_tree(('a', ('b', None, None), None))
	True
	>>> is_tree(('a', ('b', None, None)))
	False
	>>> is_tree(('a', ('b', ('d', None, None), ('e', None, None)), ('c', None, ('f', ('g', None, None), None))))
	True
	>>> is_tree(('a', None, None))
	True
	>>> is_tree(tuple([None]))
	True
	'''
	if not len(tree) == 3: return tree == tuple([None])
	for subtree in tree:
		if type(subtree) is types.TupleType: return is_tree(subtree) 
	return True



import doctest
doctest.testmod()