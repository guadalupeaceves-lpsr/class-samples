# Remember that you can also use touch to create files!
#  open a file for writing
# second argument:
# r is for reading
# r+ is for writing/reading (existing file)
# w is writing(be careful! starts writing from the beginning)
# a is append- writing *from the end*


myFile = open("num_list.txt", "w")

# create a list to write to my file
nums = range(1, 501)


# write each item to the file
for n in nums:
	myFile.write(str(n)+ '\n')

# close the file

myFile.close()



