def greet():
	global name
	name = "General the Jaguar"
	print (name)

greet()

# Since "name" is a global variable, we can use it
# outside of the "greet" function scope:
print(name)
