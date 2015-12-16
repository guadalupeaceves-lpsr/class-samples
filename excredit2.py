fave = 9
print("This is a game. Type here a number:")

user_number = int(input())

if user_number <= 8:
	print("Sorry, you lose. :( This number was too low. Try again.")

if user_number >= 10:
	print("Sorry, you lose. :( This number was too high. Try again.")

if user_number == 9:
	print("Wow, you guessed it! You must be a genius.")
