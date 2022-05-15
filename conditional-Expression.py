def sequence_class(immutable):
	"""
	this functions will return either tuple or list object, but that type dos'nt cantain any value
	eg:
	s = sequence_class('i') # since <i> == something so <immutable> is true and we get tuple, so after this call <s> is tuple type varable but it is empty
	s('amir') # return ('a', 'm', 'i', 'r') same as tuple('amir')
	"""
	return tuple if immutable else list


for i in ['i', '']:
	seq = sequence_class(i)
	s = seq('Amir saleem')
	print(s, '\n', type(s), '\n')