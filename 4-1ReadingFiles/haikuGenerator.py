# this program will ask the user for lines of code.

# once the three lines are done, it will ask the user for the name of the file.
# this is asking the user for the lines of code, and setting each of them to a variable
print("Welcome to the Haiku generator!")
print(" ")

print("Provide the first line of your haiku:")
user_firstLineOfHaiku = str(raw_input())
print(" ")

print("Provide the second line of your haiku:")
user_secondLineOfHaiku = str(raw_input())
print(" ")

print("Provide the third line of your haiku:")
user_thirdlineOfHaiku = str(raw_input())
print(" ")

# this is asking the user to write a name for the file which will have the user's haiku
print("What file would you like to write your haiku to? Remember to add .txt at the end of the name:")
user_nameOfFile = str(raw_input())
print(" ")

user_Haiku = [user_firstLineOfHaiku, user_secondLineOfHaiku, user_thirdlineOfHaiku]
userHaikuFile = open(user_nameOfFile, "w")

for haikuLine in user_Haiku:
	userHaikuFile.write(haikuLine + "\n")

# this is telling the user that everything is done, and that he/she can look at the file and 
# their haiku will be inside
print("Done! To view your haiku, type 'cat' and the name of your file at the command line.") 


userHaikuFile.close()
