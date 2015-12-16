import random
# This assigned random_luck_number to the value of a number from 1 to 10, and setting the variable to a string. 
random_luck_number = random.randint(1,10)
random_luck_number = str(random_luck_number)

#  This will print,'Welcome to Guadalupe's Quest!' and then,'Enter the name of your character:'.
#  It is asking for the character's name.
# It then assigns userplayer_name to the character's name, which would make userplayer_name into a string variable.
print("Welcome to Guadalupe's Quest!")
print("Enter the name of your character:")
userplayer_name = raw_input()
# This would print, in each line of code, everything in the quotation marks in order that it is.
#  So, if it were print("yes") and print("no"), it would print:
# yes
# no
# So, you take that, and do the same, but with everything below.
# It is basically saying that you will be able to set the character stats. 
# When the character stat numbers are added together, it should not exceed 15 or any of them be zero.
print("Rules-")
print("You are now about to set your characters stats.")
print("You will set your character's:")
print("Strength")
print("Health")
print(", and Luck.")
print("You will only be able to use 15 points in total.")
print("So, let's say that you want a health of 10, luck of 1, and strength of 2, it is possible.")
print("The numbers that you set your stats to be should not be over 15.")

# All of the variables in this code block are integer variables.
# Here, it is asking for the strength, only from the numbers 1 to 10.
print("Enter strength (1-10):")
# It is assigning userplayer_strength_number to the number that the user typed in.
userplayer_strength_number = int(raw_input())
# It is asking for the health number, and assigns userplayer_health_number to the number that the user next typed in.
print("Enter health(1-10):")
userplayer_health_number = int(raw_input())
# This is asking for the luck number, and is assigning userplayer_luck_number to the number that the user typed in.
print("Enter luck(1-10):")
userplayer_luck_number = int(raw_input())

# This is assigning user_no to the word yes, making it into a string variable.
user_no = 'yes'

# This is an if comparison statement, and would print,' You have given your character too many points!'
# If the value of the integer variable userplayer_strength_number plus the value of 
# the integer variable userplayer_health_number plus 
# the value of the integer variable userplayer_luck_number is more than 15, then it would do all of the command blocks
# below and assigned to it.
# So, it would reassign the variables userplayer_luck_number, userplayer_health_number, and userplayer_strength number to 
# 5, and turns them to string variables.
# Let's say that the value of the string variable were sting, then it would then print:
# Default values have been assigned, sting:
# strength:5, health: 5, luck: 5  
if userplayer_strength_number + userplayer_health_number + userplayer_luck_number > 15:
	print("You have given your character too many points!")
	userplayer_luck_number = str(5)
	userplayer_strength_number = str(5)
	userplayer_health_number = str(5)
	print("Default values have been assigned, " + userplayer_name + ":")
	print("strength:" + userplayer_strength_number + ", " + "health: " + userplayer_health_number+ ", luck: " + userplayer_luck_number)  
# Ths would basically do the same as the block above, but for the reason that they set at least one variable
# to the value of 0.
elif userplayer_strength_number == 0 or userplayer_luck_number == 0 or userplayer_health_number == 0:
        print("You have given your character too many points!")
        userplayer_luck_number = str(5)
        userplayer_strength_number = str(5)
        userplayer_health_number = str(5)
        print("Default values have been assigned, " + userplayer_name + ":")
        print("strength:" + userplayer_strength_number + ", " + "health: " + userplayer_health_number+ ", luck: " + userplayer_luck_number)
# If the comparison statement above was False(which means that it was not true), then it would just 
# set the variables userplayer_luck_number, and userplayer_health_number to string variables.
# It would then print the value of the string variable userplayer_name with a colon next to it.
# It would then print:
# strength: (the value of the variable userplayer_strength_number), health: (value of userplayer_health_number),
#  luck: (value of userplayer_luck_number'
# without the parenthesis, and on the same line.
else:
	userplayer_luck_number = str(userplayer_luck_number)
	userplayer_strength_number = str(userplayer_strength_number)
	userplayer_health_number = str(userplayer_health_number)
	print(userplayer_name + ":")
	print("strength: " + userplayer_strength_number + ", " + "health: " + userplayer_health_number+ ", luck: " + userplayer_luck_number)


# This will ask the user if it wants to go right or left, and will 
# set userplayer_decision_to_fork_in_road to the choice, which would make it into a string variable.
print(userplayer_name + ", you've come to a fork in the road. Do you want to go right or left? Enter 'right' or 'left'.")
userplayer_decision_to_fork_in_road = raw_input()


# This is saying that if the value of the variable userplayer_decision_to_fork_in_road is left, then
# it would ask the user if it would want to pick up a rock.
# If the user saif yes, then the user would win. If the user said no, then he or she would lose.
# Either way, it would set user_no to be the value of the work no.
if userplayer_decision_to_fork_in_road == 'left': 
	print("You have come across a pebble. Do you take it?")
	print("Write 'yes' or 'no'.")
	userplayer_take_or_not_pebble = raw_input()
	if userplayer_take_or_not_pebble == 'no':
		print("Well, you lost because you came across a zombie and could not defend yourself.")
		user_no = 'no'
	if userplayer_take_or_not_pebble == 'yes':
		print("You came across a zombie, and were able to defend yourself. You won!")
		user_no = 'no'
# If the value of the variable userplayer_decision_to_fork_in_road was right and
# the value of the variable userplayer_health_number were 11, then it would print everything right below it.
# It would also make the value of the variable 'no'.
if userplayer_decision_to_fork_in_road == 'right' and userplayer_health_number == '11':
	print("You saw a troll walking underneath a bridge. You try to cross quietly but your strength makes a loud noise.")
	print("You then decided to take it out.")
	print("There was a little problem.")
	print("The troll turned into a giant, and tried to squash you.")
	print("With your strength and health, you were able to beat the giant.")
	print("You won!")
	user_no = 'no'
# This is saying that if the user had chosen to go right, and if the value of random_luck_number were 6 or 8, 
# the player would win. It would also set the value f the variable user_no.
elif userplayer_decision_to_fork_in_road == 'right' and random_luck_number == '6' or random_luck_number == '4':
        print("You won the game!")
	user_no = 'no'
# If the user chose to go right, the health number were a number from 4 to 10, and the strength number were 5, 
# it would print everything below it and before reassigning the variable user_no to the word no. 
elif  userplayer_decision_to_fork_in_road == 'right' and userplayer_health_number > 3 and userplayer_strength_number == '5':
	print("You saw a troll walking underneath a bridge. You decided to cross quietly, but your strength made a noise.")
	print("You then decided to take it out.")
	print("There was a little problem.")
	print("The troll turned into a giant, and tried to squash you.")	
	print("You remember that you have little strength, but you decide to fight anyways.")
	print("You won the game!")
	user_no = 'no'
# This is saying that if the user chose to go right, and if the random_luck_number were equal to the numbers
# 6 or 4, then the user would win, and would set user_no to be the value of no.
elif userplayer_decision_to_fork_in_road == 'right' and random_luck_number == '6' or random_luck_number == '4':
        print("You won the game!")
	user_no = 'yes'
# With this, even if your input would usually do nothing because it was put in wrong, it 
# would print out what was in the parenthesis except for the quotation marks.
# This is saying that if the value of the variable is still yes-which means that all of the comparison statements
# were not True, then it would print what is in the quotation marks.
elif user_no == 'yes':
		print("You lost the game because Lady Gaga came in with raw-raw power, and killed you before you could do anything else. ")
# Sorry for making you read all of that, and sorry for the spelling and grammar errors.
