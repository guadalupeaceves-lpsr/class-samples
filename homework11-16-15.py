# This will print,"These are the singers in my a cappella group:"
print("These are the singers in my a cappella group:")
# This will assign acappellasingersingroup to the words,'Sasha','Kristin','Sam','Rebecca','Sean','Teddy','Tom',
# which would make it into a list variable.
acappellasingersingroup = ['Sasha', 'Kristin', 'Sam', 'Rebecca', 'Sean', 'Teddy', 'Tom']
# This will sort the list that is assigned to the list varable, acappellasingersgroup in alphabetical order
# if it were printed out.
acappellasingersingroup.sort()
# This will assign x to 1, which would make it into an integer variable.
x = 1

# This is making a variable called to current_acappellasingersingroup assigned to first the first thing
# in the list assigned to the variable acappellasingersingroup. For each thing on the list,
# everything else below it will be done that number of times.
for current_acappellasingersingroup in acappellasingersingroup:
# This will set x to be a tring variable.
	x = str(x)
# If the first thing on the list assigned to the list variable 
# acappellasigersingroup was 'Then', then this would print," 1. Then."
	print(x + ". " + current_acappellasingersingroup)
# This will set the variable x to be an int variable, allowing what it has
# been assigned to to be added to other numbers.
	x = int(x)
# This is assigning x to the past value of x added by 1, which would
# make it into an integer variable.
	x = x + 1
