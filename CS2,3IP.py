
print("You are applying to Richmond State CSU.")
print("How many miles do you live from Richmond State CSU?")
user_milesfromRichmondState = int(raw_input()) 
print("What is your GPA?")
user_GPA = float(raw_input())
print("What is your ACT test score?") 
user_ACT_test_score = int(raw_input())  
if user_milesfromRichmondState <= 30 and user_GPA >= 2.0:
	print(" You have been accepted to Richmond State CSU. Congratulations!")
else:	
	if user_milesfromRichmondState and  user_GPA >= 2.5 and user_ACT_test_score >= 18:
		print("You have been accepted to Richmond State CSU. Congratulations!")
	else:
		print("You have not been accepted to the Richmond State CSU.")
