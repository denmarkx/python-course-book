inStock = True
customerBalance = 100.32
itemPrice = 74.99

# Check if item is in stock:
if inStock:
	# It is.
	# Check if customer has enough:
	if customerBalance >= itemPrice:
		print ("Payment successful!")
	else:
		print ("Insufficient funds.")
else:
	print ("Item is out of stock.")
