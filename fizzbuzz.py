def fizzbuzz():
	array = []
	for x in range(1,101): 
		num = x
		if (num%3 == 0):
			num = "Fizz"
		array = array + [num]
	for x in array: print(x)
	return array
