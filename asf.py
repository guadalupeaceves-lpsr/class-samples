current_GPA = 1.4

eligible_to_play_GPA = 2.5
 
while current_GPA < eligible_to_play_GPA:
	 print("Study harder!")
	 print("Did your GPA improve? By how much? Write it below:")
	user_eligibility_afterwards = raw_input()
	user_eligibility_afterwards_string = str(user_eligibility_afterwards)
	user_needed_to_be_eligible = print(user_eligibility_afterwards - 2.5)
	print("Your GPA is now " + user_eligibility_afterwards_string + ", and you're " + user_needed_to_be_eligible + " from being able to play.")

