def get_volume():
	# Python automatically turns this into a tuple:
	# (5, 10, 15)
	return 5, 10, 15

# Since we return 3 values, we can assign each to its own variable:
length, width, height = get_volume()
print (length, width, height)
