# this is creating a class called Player 
# it is also creating a method that will use the arguments that the user
# will most likely enter when calling on this class
# so, if I were to create an object for this class called my_player, and call
# the function and write the arguments, like a name like Jorge,
# this will allow me to access those arguments and call them outside of this constructor

# the printStats method will only work when the argument is a list
# it will split each item in that list argument, and print each one separately

# the average_GoalNumber method will calculate (estimated in rounded numbers) the 
# average number of goals

# the saveTeam method will open a file, write to that file, and close the file
# the load team will add players from an already existing file, and adding them to this file

class Player(object):
	def __init__(self, name, age, goals, jerseynumber, position):
	 	self.name = name
		self.age = age
		self.goals = goals
		self.jerseynumber = jerseynumber
		self.position = position

	def printStats(self, list):
		for player in list:
			print(" ")
			print("Name: " + player.name)
			print("Age: " + player.age)
			print("Goals: " + player.goals) 
			print("Jersey Number: " + player.jerseynumber)
			print("Position:  " + player.position)
			print(" ")

	def averageGoals(self, playerList):
		average_goalNumber = 0
		average_goalNumberDivider = 0
		for player in playerList:
			average_goalNumber = int(player.goals) + average_goalNumber	
			average_goalNumberDivider = average_goalNumberDivider + 1
		if average_goalNumber == "0":
			average_goalNumber = 0 
		average_goalNumber = float(average_goalNumber / average_goalNumberDivider)
		print("The average number of goals for your players is " + str(average_goalNumber))

	def saveTeam(player_name, playerList, filename):
		player_name = open(filename, "w")
	       	for current_player in playerList:
	        	player_name.write(current_player.name + " " + str(current_player.age) + " " + str(current_player.goals) + " " + str(current_player.jerseynumber) + " " + current_player.position + " " + "\n")
	        player_name.close()

	def loadTeam(player_name, filename, list):
		player_name = open(filename, "r")
       		fileLines = player_name.readline()
       		while fileLines != '':
			filename_Words = fileLines.split()
       		        user_player = Player(filename_Words[0], filename_Words[1], filename_Words[2], filename_Words[3], filename_Words[4])
			list.append(user_player)
       		        fileLines = player_name.readline()
		player_name.close()
	def deletePlayer(player_name, list, player_jerseyNumber):
		for player in list:
			player_realJerseyNumber = player.jerseynumber
			if player_realJerseyNumber == player_jerseyNumber:
				list.remove(player)
				print(list)

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
	print("Welcome to Team Manager Deluxe.")
	print(" ")
	print("Do you want to start with a new team or open an existing team?")
	print("Enter the number of you choice and press Enter.")
	print("(1) Start with a new team")
	print("(2) Open a file for an existing team")
	user_fileDecision = raw_input()
	if user_fileDecision == '2':
		print(" ")
                print("What is the filename for your existing team? Enter the whole name, including its .tmd extension.")
		print("Careful! If you go through this process twice, and you type in the same file, the players will be on the list twice.")
                user_fileName = raw_input()
# this is saying that it will load already_existing
# objects that have been written in other files onto this file
		user_start = Player('nuan', 8, 4, 22, 'midfielder')
		user_start.loadTeam(user_fileName, myPlayers)
# this is asking the user what they would like to do
		print("What do you want to do? Enter the number of your choice and press Enter.")
		print("From the options below...")
		print(" ")
		print("(1) Add players")
		print("(2) Print players")
		print("(3) Print average number of goals for all players")
		print("(4) Save your player list to a file")
		print("(5) Remove a player from the team")
		print("(0) Leave the program")
# this is setting user_decisionOf_WhatToDo to the number that the user inputed, which will determine what this code will do next
		user_decisionOf_WhatToDo = str(raw_input())
# this is saying that if the value of the variable above is 0, then it 
# will change the value of the variable user_decisionToStop to the value
# of yes instead of no, which will stop this while loop, and end this program's code
		if user_decisionOf_WhatToDo == "0":
			user_decisionToStop = 'yes'
# this is saying that if the user decided to input the number one, then
		if user_decisionOf_WhatToDo == "1":	
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
			print("What is the player's jersey number? Type the number below in the required format:")
			user_playerJersey_Number = str(raw_input())
			print("What is the player's position? Type it below:")
			user_playerPosition = raw_input()
                	if user_playerGoals > 2:
                	        user_player_Three_Goals = Player(user_playerName, user_playerAge, str(user_playerGoals), user_playerJersey_Number, user_playerPosition)
                	        myPlayers_Over_Three_Goals.append(user_player_Three_Goals)
                	user_player = Player(user_playerName, user_playerAge, str(user_playerGoals), user_playerJersey_Number, user_playerPosition)
                	myPlayers.append(user_player)
# this is saying that if the value of this variable is 2, then the block of code tied to this 
# if statement will print the list of players, and their values		
		if user_decisionOf_WhatToDo == "2":
			print(" ")
			print("List Of All Players:")
			print(" ")
			user_start.printStats(myPlayers)
# this is saying that if the value of the variable is 3, then
# the averageGoal method will be called
		if user_decisionOf_WhatToDo == "3":
			user_start.averageGoals(myPlayers)
		if user_decisionOf_WhatToDo == "4":
			print("What is the name of the file that you want your players to be saved in?")
			print("Don't forget to add .tmd to the end of its name, and no numbers in it.")
			userPlayer_fileName_chosen = raw_input() 
			user_start.saveTeam(myPlayers, userPlayer_fileName_chosen)
		if user_decisionOf_WhatToDo == "5":	
			print("Which player do you want to remove from the team? Type in that player's jersey number:")
			user_delete_player_number = raw_input()
			user_start.deletePlayer(myPlayers, user_delete_player_number)
                	user_start.saveTeam(myPlayers, user_fileName)			
# this is saying that if the value of this variable is 1, then	
	if user_fileDecision == "1":
# this program will allow the user to create a completely new team to work on
# this asks the user for what they want to call the file, and assigns it to a variable as that variable's value 
		print("What is the name of the file that you want your players to be saved in?")
		print("Don't forget to add .tmd to the end of its name, and no numbers in it.")
		user_playerFileName = raw_input()
                user_start = Player("noir", 12, 2, 21, "defense")
# this asks the user for its choice, and assigns it to a variable, which determines what the code will do next
		print("(1) Add players")
		print("(2) Print players")
		print("(3) Print average number of goals for all players")
		print("(0) Leave the program")
		user_decisionChosen = raw_input()
                user_start.saveTeam(myPlayers, user_playerFileName)
# this is saying if the value of the variable is 1, then 
		if user_decisionChosen == "1":
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
			print("What it the player's jersey number?")
			user_playerJersey = raw_input()
			print("What is the player's position? (e.g., forward, midfielder, etc.")
			user_playerPosition = raw_input()
	                if user_playerGoals > 2:
	                        user_player_Three_Goals = Player(user_playerName, user_playerAge, str(user_playerGoals), str(user_playerJersey), user_playerPosition)
	                        myPlayers_Over_Three_Goals.append(user_player_Three_Goals)
	                user_player = Player(user_playerName, user_playerAge, str(user_playerGoals), str(user_playerJersey), user_playerPosition)
                	myPlayers.append(user_player)
# this is saying that if the value of this variable is 2, then the block of code tied to this 
# if statement will print
	        if user_decisionChosen == "2":
# the user has made the choice of which list they will access, and their decision
# will determine the list that will be printed on the terminal page
                	print("(1) List Of All Players")
                	print("(2) List Of Players With 3 Or More Goals")
                	print("Type in the number assigned to the list that you want to access below in 3,2,8 format:")
                	user_listToAccess = str(raw_input())
                	if user_listToAccess == "1":
                	        print(" ")
	                        user_player.printStats(myPlayers)
	                if user_listToAccess == "2":
	                        print(" ")
	                        user_player_Three_Goals.printStats(myPlayers_Over_Three_Goals)
# if the value of this variable is 3, then
		if user_decisionChosen == "3":
# it will calculate the average number of goals in the user's list
                        user_start.averageGoals(myPlayers)
		# this is saying that if the value of the variable above is 0, then it 
# will change the value of the variable user_decisionToStop to the value
# of yes instead of no, which will stop this while loop, and end this program's code
                if user_decisionChosen == "0":
                        user_decisionToStop = 'yes'
