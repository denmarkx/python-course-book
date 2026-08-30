# Since "name" has a default value, 
# "punctuation" is required to have one as well.
def greet(greeting, name="General the Jaguar", punctuation='!'):
	print (greeting, ',', name, punctuation)

greet("Hello")

# The same goes for when explicitly writing
# the parameter name in the function call:
greet("Hello", name="Rowdy the Roadrunner", punctuation="?")

# Wrong! "punctuation" must be specified
# since "name" is explicitly written here.
# greet("Hello", name="Rowdy the Roadrunner")
