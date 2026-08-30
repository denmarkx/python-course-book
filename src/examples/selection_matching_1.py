grade = 'A'
match grade:
	# Equivalent to: if grade == 'A'
	case 'A':
		// ..then
		print ("Awesome!")

	# Equivalent to else.
	case _:
		print ("Oh no!")
