#!/usr/bin/env python3 

######################
#### uses_only.py ####
######################

# Take a word and a string of letters as separate inputs and return TRUE if the word contains only the letters in the list

# For example, to use this program:
# uses_only.py
# Word: strings
# Letter list: string
# True

##############
#### Main ####
##############

def uses_only():

	# Parse input
	input_word = str(input("Word: "))
	letter_list = str(input("Letter list: "))

	# Compress input word to unique values
	# Push both to lists and sort
	input_word = sorted(set(input_word))
	input_list = sorted(list(letter_list))
	
	#print(input_word)
	#print(input_list)
	
	# Iterate over zipped iterator and check match
	# If they match, don't add anything to the counter
	# If they don't match, add 1 to the counter 
	counter = 0
	for i, j in zip(input_word, input_list):
		if i == j:
			counter += 0
		else:
			counter += 1
	
	if counter == 0:
		print(True)
	else:
		print(False)

uses_only()
