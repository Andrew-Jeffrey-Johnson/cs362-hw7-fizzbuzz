def fizzbuzz():
	array = []
	for x in range(1,101): 
		num = x
		if (num%3==0 and num%5==0):
			num = "FizzBuzz"
		elif (num%3 == 0):
			num = "Fizz"
		elif (num%5 == 0):
			num = "Buzz"
		array = array + [num]
	for x in array: print(x)
	return array
