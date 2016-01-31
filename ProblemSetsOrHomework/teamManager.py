
class Player(object):
	def __init__(self, name, age, goals, games):
		self.name = name
		self.age = age
		self.goals = goals
		self.games = games
# this will add a user to the list
	def AddPlayer(self):
		if user_decisionForList == "add":
			print(" ")
			print("Hello! You have decided to add a player.")
        	        print("Do you truly want to add a player or not? If yes, then type 'start'. If not, then type 'leave'")
        	        answerToQuestion = str(raw_input())
        	        if answerToQuestion == "start":
				print(" ")
        	                print("We will now start adding a player.")
        	                print("Type in the name of the player now:")
        	                user_name = str(raw_input())
        	                print("Type in the age of the player you want to add.")
        	                user_age = str(raw_input())
        	                print("How many goals has he or she made in his/her whole career?")
        	                user_goals = str(raw_input())
        	                print("How many games has he/she played? Type in the number")
        	                user_games = str(raw_input())
				user_Player = Player(user_name, user_age, user_goals, user_games)
			if answerToQuestion == "leave:":
				print("We will now leave.")
		def PrintPlayers(self):
# this will print the list for the user
			print(" ")
                	print("Do you truly want to see the list of players? Type in 'start' to start, and 'leave' to leave")
                	user_leave_or_stay = str(raw_input())
                	if user_leave_or_stay == "leave":
				print(" ")
                	        print("Have a good day!")
                	if user_leave_or_stay == "stay":
				print(" ")
                        	print("OK, we will now print the information.")
	
		               
# this is the first thing that will happen
# this asks the user what they want to do

print("You are accessing this team's list. Do you want to do that? Type 'yes' or 'no'")
user_decision = str(raw_input())
if user_decision == "no":
        print("We are sorry for having taken you time. Goodbye.")
        user_decision = "stop"
while user_decision == "yes":
        print("Hello! Would you like to add a player, or would you like to see the list?")
        print("Type 'print' to see the list, or type 'add' to add a player to the list.")
        user_Player = Player()
	user_decisionForList = str(raw_input())

	if user_decisionForList == "add":
		self.AddPlayer()
	if user_decisionForList == "print":	
		self.PrintPlayers()
	print("Do you want to stop going? Type in 'no' if you want to leave, and 'yes' if you don't want to leave.")
	user_decision = str(raw_input())
	if user_decision == "no":
		print(" ")
		print("Thank you for your time and patience.")
