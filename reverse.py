friendsandfamilynames = ["Brenda","Kimberly","Jennifer","Armando","Alicia","Mariana","Angy","Lidia","Elizabeth","Nancy"] 
il = 0
friendsandfamilynames.sort()
friendsandfamilynames.reverse()
print("These are the 5 friends and family I spend the most time with:")
print(" ")

for current_name in friendsandfamilynames:
	il= 1 + il
	current_name = str(current_name)
	print(str(il) + ". " + str(current_name))
