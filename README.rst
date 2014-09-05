
Unroll
======
Multi-line comprehensions; Python 2/3 compatible; list-comprehensions, generators, dict-comprehensions, and more.

Unroll is a 'vernacular' tool, intended for everyday Python programming.

The most common use-case is the ``@unroll`` decorator, for writing the equivalent of multi-line comprehensions::

	@unroll(list)
	def evens():
	    for i in range(5):
	        yield 2*i
	        
	assert callable(evens)
	assert evens() == [0, 2, 4, 6, 8]

The argument into decorator determines the type of comprehension. Use ``list`` for a list-comprehension, ``dict`` for a dict-comprehension (this works in Python 2.6), and ``iter`` for generators (this is the default if nothing is provided.

For an even more direct equivalent to multi-line comprehensions, try the ``\@compr`` decorator, which immediately invokes the resulting function, resulting in a variable rather than a function::

	@compr(list)
	def evens():
		for i in range(5):
			yield 2*i
			
	assert isinstance(evens, list)
	assert evens == [0, 2, 4, 6, 8]


