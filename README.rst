===========================
	Unroll
===========================
A core vernacular tool, for everyday Python programming.
The most common use-case is in writing the equivalent of multi-line comprehensions.

	@unroll(list)
	def evens():
	    for i in range(5):
	        yield 2*i
	assert callable(evens)
	assert evens() == [0, 2, 4, 6, 8]

	For an even more direct equivalent, use:
	
	@compr(list)
	def evens():
		for i in range(5):
		yield 2*i
	assert isinstance(evens, list)
	assert evens == [0, 2, 4, 6, 8]
	
	