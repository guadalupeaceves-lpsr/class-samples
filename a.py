print("What is your GPA? Write in decimal form below:")
current_GPA = float(raw_input())

eligible_to_play_GPA = 2.5

while current_GPA < eligible_to_play_GPA:
        print("Study harder!")
	print("Did your GPA go up or down?")
	user_up_or_down = raw_input()
	if user_up_or_down == 'down':
		current_GPA = current_GPA - .1
	if user_up_or_down == 'up':
		current_GPA = current_GPA + .1
	current_needed = str(eligible_to_play_GPA - current_GPA)
	current_GPA = str(current_GPA)
	print("Your GPA is now " + current_GPA + ", and you're " + current_needed + " away from being able to play.")
	current_GPA = float(current_GPA)
