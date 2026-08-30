def power(exponent):
	def calculate(base):
		# Remembers the "exponent" variable
		# from the outer function.
		return base ** exponent

	# Returns the function: "calculate".
	# This does NOT call the calculate function.
	return calculate

# Returns the "calculate" function where
# "exponent" is remembered as 2.
square = power(2)

# Returns the "calculate" function where
# "exponent" is remembered as 3.
cube = power(3)

print(square(4))
print(cube(4))
