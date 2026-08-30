def outer(message):
	# Nested function:
	def inner():
		print (message)

	# Call inner function.
	inner()

# Call outer function.
outer("Hi there!")

"""
Since the inner function is defined
within the outer function, we cannot
call it outside of the function.
"""
# inner() # Error!
