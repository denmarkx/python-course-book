def outer_func():
	# "name" is a local variable
	# attached the the "outer_func" scope.
	name = "General the Jaguar"

	def inner_func():
		nonlocal name
		# The variable "name" belongs to
		# the "outer_func" scope.
		name = "Rowdy the Roadrunner"

	inner()
	print (name)
