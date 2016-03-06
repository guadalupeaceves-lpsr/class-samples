# this is creating a class called Player 
# it is also creating a method that will use the arguments that the user
# will most likely enter when calling on this class
# so, if I were to create an object for this class called my_player, and call
# the function and write the arguments, like a name like Jorge,
# this will allow me to access those arguments and call them outside of this constructor
# the printStats method will only work when the argument is a list
# it will split each item in that list argument, and print each one separately
class Player(object):
	def __init__(self, name, age, goals):
	 	self.name = name
		self.age = age
		self.goals = goals
	def printStats(self, list):
		for player in list:
			print(" ")
			print("Name: " + player.name)
			print("Age: " + player.age)
			print("Goals: " + player.goals) 
			print(" ")

# this is creating an empty list that we will add onto later in this code
myPlayers = []
myPlayers_Over_Three_Goals = []
# this is setting this to the value of the word no
user_decisionToStop = 'no'

# this is saying that while the value of the variable user_decisionToStop is no,
# then all of the code attached to this statement will continue to be repeated, 
# meaning that it will be an infinite loop if you do not change this variable's value
while user_decisionToStop == 'no':
# this will print whatever is in the quotation marks, all on each separate line
# when you run this program on the Terminal page
	print("Hello. You are now accessing this team manager program.")
	print(" ")
	print("From the options below...")
	print("(1) Add players")
	print("(2) Print players")
# this is asking the user what they would like to do, to type in their choice
	print("Which one would you choose? Type in the number assigned to that option below:")
# this is setting user_decisionToAdd_or_Print to whatever the user decided to input on the
# Terminal page
	user_decisionToAdd_or_Print = str(raw_input())
# this is saying that if the user decided to input the number one, then
	if user_decisionToAdd_or_Print == "1":	
# it would print everything in the quotation marks on the Terminal page right below
		print(" ")
		print("You are about to add players to the list.")
		print(" ")
# this is asking the user the information needed to create a Player object
# to put through the Player class, and creating a variable to assign to each
# piece if information
# it is also appending certain things to a list
		print("What is the name of the player? Type it below:")
		user_playerName = raw_input()
		print(" ")
		print("What is the player's age? Type it below(e.g. 1, 2, 3 10, etc.):")
		user_playerAge = str(raw_input())
		print("How many goals has the player made? Type the number below in 5, 4, form:")
		user_playerGoals = int(raw_input())
                if user_playerGoals > 2:
                        user_player_Three_Goals = Player(user_playerName, user_playerAge, str(user_playerGoals))
                        myPlayers_Over_Three_Goals.append(user_player_Three_Goals)
                user_player = Player(user_playerName, user_playerAge, str(user_playerGoals))
                myPlayers.append(user_player)
# this is saying that if the value of this variable is 2, then the block of code tied to this 
# if statement will print		
	if user_decisionToAdd_or_Print == "2":
		print(" ")
		print("(1) List Of All Players")
		print("(2) List Of Players With 3 Or More Goals")
		print("Type in the number assigned to the list that you want to access below in 3,2,8 format:")
		user_listToAccess = str(raw_input())
# the user has made the choice of which list they will access, and their decision
# will determine the list that will be printed on the terminal page
		if user_listToAccess == "1":
			print(" ")
			user_player.printStats(myPlayers)
		if user_listToAccess == "2":
			print(" ")
			user_player_Three_Goals.printStats(myPlayers_Over_Three_Goals)
# this will print what is in the parenthesis, and it will assign the variable to the user's decision
	print(" ")
	print("Do you want to stop? Type 'yes' or 'no'.")
	user_decisionToStop = raw_input()
