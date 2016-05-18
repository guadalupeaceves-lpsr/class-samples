# applyCipher.py
# A program to encrypt and decrypt user text
# using Caesar's Cypher
# 
# Author: rc.aceves.guadalupe [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):
	# placeholder
	return {}

# asks the user to input the encoded message
# arguments: none
# return: encoded message
def getMessage():
	pass

# for each letter in the message, decodes and records
# arguments:encoded message, dictionary
# returns:decoded message
def decodeMessage(message, dictonary):

	pass

# outputs the message to the terminal
# arguments: the decoded message to the terminal
# returns: none
def printMessage(message, dictionary):
	pass

# execution starts here

# ask user for the key
print("What key would you like to decode?")
key = int(raw_input())

dictionary = createDictionary(key)

message = getMessage()

decodedMessage = decodeMessage(message, dictionary)

printMessage(decodedMessage)
