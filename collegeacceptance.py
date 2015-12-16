print("How old are you?")

age = int(input())

print("What is you GPA?")
GPA = float(input())
	
# if GPA is over 3.0 and age is over 16, accept
if GPA > 3.0 and age > 16:
	print("You have been accepted. Congrats!")
else:
	print("Sorry, guess you'll have to go to Harvard instead.")
 
