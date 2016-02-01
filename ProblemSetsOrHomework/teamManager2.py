# This is setting the variable to "yes".
user_decision_continue = 'yes'

# This is allowing certain variables(information) to be accessed in an easier way.
class Player(object):
	def __init__(self, name, age, games, goals):
		self.name = name
		self.age = age
		self.games = games
		self.goals = goals	
# this will add a player to the list
	def AddPlayers(self):
		myListOfPlayers = myListOfPlayers + list

# this will print the list of players
	def PrintWholePlayers(self, list):
		print(" ")
		for current_information in list:
			number = 0
			print(current_information)		
			print(" ")

# this will print specific player by asking the user for the player's name.
# this will ask the user if they want to access the team player's list
# this is creating a list
myPlayersList = []
 
# This is taking two paths depending on the user's decision in the code above. 
# One allows the code to continue(access list), and one stops it(no access to list).
while user_decision_continue == "yes":
# this will print specific player by asking the user for the player's name.
# this will ask the user if they want to access the team player's list.
	print(" ")
	print("Hello. You are about to access this soccer team's player list.")
	print("Do you want to access it? Type 'yes' to access it, and 'no' to not access the list.")
	user_decision_continue = str(raw_input())
	print("Do you want to add a player to the list, or do you want to print the list?")
	print("Type 'add' to add a player, and 'print' to print the list.")
	user_add_or_print = str(raw_input())
# this is asking the user if he/she wants to add a player to the list.
	if user_add_or_print == 'add':
		print(" ")
		print("You are about to add a player to this team's list.")
# this is what will decide the course of action in the code because of the user's decision.
# this is asking the user for the info to add to the list
		print(" ")
		print("What is the player's name?")
		user_name = str(raw_input())
		print("What is the player's age?")
		user_age = str(raw_input())
		print("What is the number of games the player has been in? If none, then write '0'.")
		user_games = str(raw_input())
		print("What is the number of goals that the player has made? If none, then write '0'.")	
		user_goals = str(raw_input())
		myPlayer = myPlayersList.append(Player(user_name, user_age, user_games, user_goals))
# this is saying that if the user has not decided to add a player, then it won't.
# this is asking the user if he/she wants to print the list of players.
	if user_add_or_print == 'print':
		print(" ")
		print("You are about to view this team's list.")
		print(" ")
# this is asking the user if he/she wants to print all of the players, or some
		print("Do you want to view all of the players? Type 'all' or nothing.")
		user_decision_printing = str(raw_input())
		if user_decision_printing == 'all':
			self.PrintWholePlayers(myPlayersList)		
	print(" ")
	print(" Do you want to continue to do this? Type 'yes' or 'no'.")
	user_decision_continue = str(raw_input())
	if user_decision_continue == "no":
		print("Thank you for your time. Goodbye.")
