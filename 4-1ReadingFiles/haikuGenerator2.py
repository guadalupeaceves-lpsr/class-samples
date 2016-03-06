# this will import a module called random that some other coder created
import random
# this program will ask the user for lines of code.

# once the three lines are done, it will ask the user for the name of the file.
# this is asking the user for the lines of code, and setting each of them to a variable
print("Welcome to the Haiku generator!")
print(" ")

# this is assigning values to certain variables
a = "Pierce one's heart with love"

b = "Reflecting water"

c = "Our Wandering souls"

d = "My cookie cutter"

e = "A rhythm created"

f = "Smiling is hoping "

g = "Did you kick the dog?"

h = "The fresh scent of spring"

i = "Can you touch you toes?"

j = "Dance to create art"

# this is asking the user which path they want to take with the first haiku line
# that means that they are able to create their own haiku line, or 
# get a random haiku line
print("Would you like to write your own first line, or get a randomize first line?")
print("Type 'random line' for a random line, and 'own line' to be able to make your own haiku line.")
print(" ")
user_decisionForFirstHaikuLine = str(raw_input())

if user_decisionForFirstHaikuLine == "random line":
	random_firstHaikuLine = [a, b, c, d, e, f, g, h, i, j]
	user_firstLineOfHaiku = random.choice(random_firstHaikuLine)

if user_decisionForFirstHaikuLine == "own line":
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
print("You will be able to view your haiku if you type...")
print(" cat, space, and then the file's name at the command line.")
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
