# this is importing a module( code that somebody else created that we want to access) called time
import time

# this will print everything that is in the quotation marks, and is asking the user for its option
print("Hi, welcome to the Haiku Reader!")
print("Choose...")
print("(1) For a haiku about  issues with technology.")
print("(2) For a haiku about random stuff.")
print("(3) For a haiku about a silly person.")
print("(4) For a haiku about writing haiku.")
print(" ")
print("Type in the number below:")
# this will assign user_chooseHaikuNumber to the number that the user typed in in its string version
user_chooseHaikuNumber = str(raw_input())

# this is saying that if the value of user_chooseHaikuNumber is 1, then it will set user_chooseHaiku to haiku1.txt, which is a text file 
if user_chooseHaikuNumber == '1':
	user_chooseHaiku = 'haiku1.txt'

# this is saying that if the value of the variable user_chooseHaiku is 2, then it will set
# user_chooseHaiku to the text file, haiku2.txt in my own directory
if user_chooseHaikuNumber == '2':
	user_chooseHaiku = 'haiku2.txt'

# this is saying that if the value of the variable user_chooseHaikuNumber is 3, then it will set
# user_chooseHaiku to the text file, haku3.txt
if user_chooseHaikuNumber == '3':
	user_chooseHaiku = 'haiku3.txt'

# this is saying that if the value of the variable user_chooseHaikuNumber is 4, then it will
# set user_chooseHaiku to the text file, haiku4.txt
if user_chooseHaikuNumber == '4':
	user_chooseHaiku = 'haiku4.txt'

# this is saying that haikuToOpen will become the class open's object, and the 
# text file assigned to user_chooseHaiku, as determined above, will be one of the arguments
haikuToOpen = open(user_chooseHaiku, "r")

# this is printing what is in the quotation marks
print("Do you want to print it all at once, or wait for a specific time to be given each line?")
print("Type 'specific', or 'at once' below:")
# this is assigning user_chooseTime to the words that the user typed in
user_chooseTime = str(raw_input())
# this will print nothing, but take up a whole line
print(" ")

# this is saying that if the value of the variable user_chooseTime is 'at once', then it
# will print the text file(argument) in the object, haikuToOpen
if user_chooseTime == 'at once':
	print(haikuToOpen.read())
	
# this is saying that if the value of the variable user_chooseTime is 'specific, then
# it will ask the user for a number in which the program will user
# to determine how fast it will print each line in the text file on the terminal page
# as the argument
if user_chooseTime == 'specific':
	print(" Type in the number of seconds that you want the program to take to print each line")
	print("below:")
	user_time = int(raw_input())
	print(" ")
	lineToPrint = haikuToOpen.readline()
# this will allow each line to print with intervals between each line
	while lineToPrint != "":
		print(lineToPrint)
		lineToPrint = haikuToOpen.readline()
		time.sleep(user_time)
# this stops the loop from continuing
	user_chooseTime = 'no'
