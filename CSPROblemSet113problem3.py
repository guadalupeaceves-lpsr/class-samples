# This will most likely allow the user to type in something that can be recorded.
import sys
# This will print, "Welcome to PumaPix!"
print("Welcome to PumaPix!")
# This will print, "Enter youor 5 favorite shows."
print("Enter your 5 favorite shows.")
# This is assigning values to variables. 
# x is assigned to the value of 0
# y is assigned to the value of 0
# x is assigned to the value of 0
# show_names is assigned to an empty list
# shows_list is assigned to a list with, "Breaking Bad", and "The Wire" in it
x = 0
y = 0
show_names = []
shows_name = []

# This is saying that if the value of the variable x is not 'done', then it would
# continue to go through all of the other codes underneath this while statement.
while x != "done":
	print("Enter a show name:")
	print("If you want to stop entering show names, enter 'done'.")
	show_name = raw_input()
	show_names.append(show_name)
	shows_name.append(show_name)
	if show_name == "done":
		x = "done"
		show_names.remove("done")
# This will print nothing, but would leave an empty space.
print(" ")
# This would print, "OK, here's what you entered:"
print("OK, here's what you entered:")
# This would print the value of the variable show_names, so the list.
print(show_names)

# This would print nothing, but would take up a line.
print(" ")
# This would print,
# "We've removed the terrible shows from your list and added a couple of important ones."
print("We've removed the terrible shows from your list and added a couple of important ones.")
show_names.sort()
# This would set show_names to the value of the two variables show_names and shows_namesadded,
# so the two of the lists together.
show_namesadded = ["Breaking Bad", "The Wire"]
show_names = show_names + show_namesadded
show_names.sort()
# This would set the list assigned to the variable show_names in alphabetical order. 
show_names.sort()
# This would sort out the contents of the list assigned to show_names
# in alphabetical order.
# This is creating a variable called current_show_names, which would be assigned to 
# a new content from the list assigned to the variable, show_names.
# It is saying that y would be assigned to the value of the variable y plus 1.
# This would print, "(The value of y). (the value of current_show_names)"

for current_show_names in show_names:
	y = int(y) + 1
	print(str(y) + ". " + current_show_names)
	
