def fizz_buzz(i):
	
	if i % 3 == 0 and i % 5 == 0:#check if fizzbuzz is divisible by 3and 5 and return fizzbuzz
		return "FizzBuzz"
	
	elif i % 3 == 0:#check if fizzbuzz is divisible by 3 and return fizz
		return "Fizz"
	
	elif i % 5 == 0:#check if fizzbuzz is divisible by 5 and return buzz
		return "Buzz"
	
	return i
