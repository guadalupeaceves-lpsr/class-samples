# This will allow the us to make a variable with the user's input.
import sys
# Ths will print, "Welcome to PumaPix!"
print("Welcome to PumaPix!")
# This will print, "Enter your 5 favorite shows."
print("Enter your 5 favorite shows.")
# This will assign x to 0, making it an integer variable.
x = 0
# This is assigning shows_list to an empty variable, making it a list variable.
shows_list = []
# This is settin y to be 0.
y = 0

# This is saying that until the value of the variable x is more than 4, it will keep
  # on following the rest of the code.
while x <  5:
# This will print, "Enter a show name:"
        print("Enter a show name:")
# This will assign show_name to whatever the user as printed, making it into a string variable.
        shows_name = [str(raw_input())]
# This will allow the list variable, shows_list, to add the user's input to it list.
        shows_lists = shows_name + shows_list
# This will assign x to the value of its past self plus 1.
        x = x + 1

# This creating a variable called show_name_in_list,
#  that will be assigned to something in the list assigned to the variable shows_list.
# So, this will continue until there is nothing left in the list, and show_name_in_list
# will always be assigned to the new listed thing.
for show_name_in_list in shows_list:
# This will print, "OK, here's what you have entered:"
        print("OK, here's what you have entered:")
# This will assign y to 1, making y an integer variable.
# If the value of the variable at the time was 3, and the value of the variable shows_list Breaking Bad,
# then this would print,
# "3. Breaking Bad"
# this is assigning y to the value of its past self, plus 1
# This is creating a variable called show_name_in_list, which would be assigned to something new
        y = int(y) + 1
        print(str(y) + ". " + str(show_name_in_list)

# This will print, in a single line, "We've removed the terrible shows from your list and added
# a couple of important ones.
print("We've removed a few bad shows and added some important ones.")
# This is creating a variable called show_name_in_list that will be assigned to a new
# thing on the list assigned to the variable shows_list, and will keep on doing the 
# code below until there are no more things left in the list of the variable 
# shows_list to be assigned to show_name_in_list.
# These will delete CSI, NCIS, add Breaking Bad, and The Wire from the list
# assigned to the variable shows_list. 
shows_list.remove("CSI")
shows_list.remove("NCIS")
show_name_in_list.append("Breaking Bad")
show_name_in_list.append("The Wire")
# this is assigning x to 1
x = 1

for show_name_in_list in shows_list:
# This will print, "(the value of x). (the value of show_name_in_list)"
        print(str(x) + ". " + str(show_name_in_list))
# This will assign x to the value of the variable x plus 1.
        x = x + 1
