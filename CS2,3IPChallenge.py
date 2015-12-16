# LPS 11th grader using this program to see 
#if they are likely to be admitted to Richmond State next year

# edit pprogram to give hepful tips like:
# "You'll need a GPA that is .3 higher than your current GPA"
# " Your ACT score is not high enough-you should enroll in a prep class")




print("You are applying to Richmond State CSU.")
print("How many miles do you live from Richmond State CSU?")
user_milesfromRichmondState = int(raw_input()) 
print("What is your GPA?")
user_GPA = float(raw_input())
user_GPAtype2 = int(user_GPA)
print("What is your ACT test score?") 
user_ACT_test_score = int(raw_input())  

if user_milesfromRichmondState <= 30 and user_GPA >= 2.0:
	print(" You have been accepted to Richmond State CSU. Congratulations!")
else:	
	if user_milesfromRichmondState and  user_GPA >= 2.5 and user_ACT_test_score >= 18:
		print("You have been accepted to Richmond State CSU. Congratulations!")
	else:
		print("You have not been accepted to the Richmond State CSU.")


user_improvement_NumberV1 = str(2.0 - user_GPA)
user_improvement_NumberV2 = str(2.5 - user_GPA)

if user_GPA < 2.0 and user_milesfromRichmondState <= 30:
	print("You need to improve your GPA score by " + user_improvement_NumberV1 + " to get accepted.")


user_ACT_Improvement = str(18 - user_ACT_test_score)	
if user_ACT_test_score < 18 and user_milesfromRichmondState > 30:
	print("You need to improve your ACT test score by " + user_ACT_Improvement + " to get accepted. ")
	print("You should also enroll in a prep class.")

if user_milesfromRichmondState > 30 and user_GPA < 2.5:

	print("You need to improve your GPA score by " + user_improvement_NumberV2 + " to get accepted.")
