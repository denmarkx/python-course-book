grade = 'A'
match grade:
	# Equivalent to: if grade == 'A'
	case 'A':
		// ..then
		print ("Awesome!")

	case 'B':
		print ("Cool!")

	case 'C':
		print ("Fair..")

	# Equivalent to else.
	case _:
		print ("Oh no!")
