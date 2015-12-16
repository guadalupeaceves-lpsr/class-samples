def length(myList):
        myLength = 0
        for x in myList:
                myLength = myLength + 1
        return myLength
 
brothers = ['Mike', 'Joe', 'Ty']
sisters = ['Lena', 'Gina']
 
print("There are " + str(length(brothers)) + " brothers.")
print("There are " + str(length(sisters)) + " sisters.")

