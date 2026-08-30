def get_mascot():
	return "TAMUSA", ("General the Jaguar", "Jaguar")

# We can mirror the structure of the return value:
university, (name, species) = get_mascot()
print (university)
print (name)
print (species)
