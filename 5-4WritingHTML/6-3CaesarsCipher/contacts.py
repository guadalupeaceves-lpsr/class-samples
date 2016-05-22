# this allows the program to get the contact information
# arguments: dictionary_name, contact_name, contact_number
# returns:none
def getNumber(contacts_list, contact_name, contact_number):
	contacts_list[contact_name] = contact_number	
# this allows the user to print all of the contacts
# arguments: dictonary
# returns: contacts' name and number
def printContacts(contacts_list):
	for contact in contacts_list:
		print(" ")
		print(contact + ": " + contacts_list[contact])
# this allows the user to print a certain contact
# arguments: name and dictonary
# returns: that specific's contact information
def accessContacts(contacts_list, name):
	for contact in contacts_list:
		if contact == name:
			print(" ")
			print(contact + ": " + contacts_list[contact])
# this will remove a contact from the list
# arguments: dictionary, name
# returns: none 
def removingContact(contacts_list, name):
	print(" ")
	del contacts_list[name]
# this will allow the user to change a contact from the list
# argument: directory, name
# returns: none
def changeContact(contacts_list, name):
	print(" ")
	print("What do you want to change? The 'name', 'number', or 'both'? Type it below:")
	decision_made = raw_input()
	if decision_made == 'name':
		print(" ")
		print("What is the new name that you want the contact to have now? Type it below:")
		new_name = raw_input()
	if decision_made == 'number':
		print(" ")
		print("What is the new number that you want the contact to have now? Type it below:")
		new_number = raw_input()
	if decision_made == "both":
		print(" ")
		print("What is the new name that you want the contact to have now? Type it below:")
		new_name = raw_input()
		print(" ")
		print("What is the new number that you want the contact to have now? Type it below:")
		new_number = raw_input()
	if decision_made == "name":
		new_number = contacts_list[name]
	if decision_made == "number":
		new_name = name
	contacts_list[new_name] = new_number
	del contacts_list[name]
# this is setting a value of 0 to the variable that allows the loops to begin
user_decision = "0"
# this is creating an empty dictionary to use later
my_Dictionary = {}

# this is a loop that will continue until decision is not equal to 0
while user_decision == "0":
# this asks the user for their decision
	print(" ")
	print("Hello, and welcome to to Contacts.app")
	print("You have three choices:")
	print("Add a phone number (1)")
	print("Print the full list of contacts (2)")
	print("Retrieve a contact number (3)")
	print("Delete a contact (4)")
	print("Change a contact (5)")
	print("Exit the app (6)")
	decision = raw_input()
# this is saying that if their decision was 1, then they  will add a contact
	if decision == "1":
		print(" ")
		print("What is the name of the contact?")
		name = raw_input()
		print(" ")
		print("What is the number of the contact? Type the dashes:")
		number = str(raw_input())
		phone_number = getNumber(my_Dictionary, name, number)
# this is saying that if their decision was 2, then they will print all of the contacts
	if decision == "2":
		print(" ")
		print("Here is the list of your phone numbers:")
		contacts_list = printContacts(my_Dictionary)
# this is saying that if their decision was 3, then they will print a specific contatc		
	if decision == "3":
		print(" ")
		print("What is the name of your contact?")
		contact_name = raw_input()
		contact_Name = accessContacts(my_Dictionary, contact_name)
# this will delete a contact
	if decision == "4":
		print(" ")
		print("What is the name of the contact that you want to delete?")
		contact_name = raw_input()
		delete_Contact = removingContact(my_Dictionary, contact_name) 
# this is saying that if their decision was 5, then they will exit the program
	if decision == "5":
		print(" ")
		print("Type the name of the contact:")
		contact_name = raw_input()
		change_contact = changeContact(my_Dictionary, contact_name)		
	if decision == "6":
		print(" ")
		print("Thank you for coming! Goodbye!")
		user_decision = "1"
