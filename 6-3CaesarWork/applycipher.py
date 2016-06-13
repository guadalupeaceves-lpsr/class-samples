import string
from string import ascii_letters as al
from itertools import izip
from collections import deque

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
	key = int(key)
# the other way around
	alphabet_List = dict((y,x) for x, y in enumerate(al, 1))
	print(alphabet_List)
	alphabet2 = dict((y,x) for y, x in enumerate(al, 1))
	print(alphabet2)
	for x in alphabet_List:
		for y in alphabet2:
			number = (int(y) + key) % 128
			if number == 0:
				number = 1
			if x == (alphabet2[y]):
				value = alphabet2[number]
				alphabet_List[x] = value
	print(alphabet_List)
        return alphabet_List

# asks the user to input the encoded message
# arguments: none
# return: encoded message
def getMessage():
	print("What is the message that you want to decode?")
	user_message = ()
	user_message = raw_input()
	return user_message

# for each letter in the message, decodes and records
# arguments:encoded message, dictionary
# returns:decoded message
def decodeMessage(message, dictionary):
	my_string = ''
	for character in message:
		for x in dictionary:	
			if x == character:
				newLetter = dictionary[x]
				my_string = my_string + str(newLetter)
	return my_string

# outputs the message to the terminal
# arguments: the decoded message to the terminal
# returns: none
def printMessage(message, dictionary):
	print(message)

# execution starts here

# ask user for the key
print("What key would you like to decode?")
key = int(raw_input())

dictionary = createDictionary(key)

message = getMessage()

decodedMessage = decodeMessage(message, dictionary)

printMessage(decodedMessage, dictionary)
