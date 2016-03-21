class Numbers(object):
	def __init__(self, number):
		self.number = number
# this will define isPrime to all of the code that it is assigned to
# this will take an argument
	def isPrime(Objectname, number, list):
# this will create a variable with a list of numbers
		numberList = range(1, int(number))
# this is saying that while there is a number in the list,
# then the loop will continue
# also the current number in the list(it moves on to the next thing on its list
# (once it has completed the code below once more)
# it will take that current number on the list, and make it into the variable current_number's new value(will be reset each
# time the code has been finished)
# this will create a variable with the value of the argument number minus 2
		algorithm = number - 2
# thiw will create a variable with the value of 0
		deciding_primeNumber = 0
		for current_number in numberList:
# this is saying that the value of the variable current_number will be assigned to 
# the argument number's value divided by the current value of the variable dividingnumber, and whatever the 
# leftover(remainder) of that arithmetic will be the value assigned
# to the variable current_number
			afterAlgorithm_number = int(number) % int(current_number)
			if afterAlgorithm_number != 0:
# this creates a variable that adds 1 to its previous value
				deciding_primeNumber = deciding_primeNumber + 1
# this is saying that if the value of both variables are the same, then
				if deciding_primeNumber == algorithm:
# this will add the number to the file
					list.append(x)
					
PrimeList = []
# this is creating a variable with the numbers 2 to 100,000
numbersVariable = range(2,100001)
# x will change to the number currently in the range of the variable numbersVariable
# this is saying that if there is still a number in the variable numberVariable, its range, then it will continue its loop
for x in numbersVariable:
	numberObject = Numbers(x)
# this is saying that the value of the variable numberObject will be changed to 
# whatever the value(or number) assigned to x is
# isPrime is a functiion, and x has become an argument for it
# the x variable will pass through the isPrime function's code
	numberObject.isPrime(x, PrimeList)
# this is saying that for the number in the list, it will continue the code attached to this for loop
numberObject = open("primes.txt", "w")
for x in PrimeList:
	numberObject.write(str(x) + "\n")

numberObject.close()

