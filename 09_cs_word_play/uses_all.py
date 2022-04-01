#!/usr/bin/env python3

######################
#### uses_only.py ####
######################

# This function takes a word and a string of required letters and returns True if the word uses all of the required letters at least once

# For example, calling the function from the command line:
# ./uses_only.py
# Word: strings
# Required letters: string
# True

# And another example, again from the command line:
# ./uses_only.py
# Word: apple
# Required letters: aples
# False

##############
#### Main ####
##############

def uses_all():

	# Parse input
	word = str(input("Word: "))
	required_letters = str(input("Required letters: "))
	
	# Count the number of occurrences of each required letter
	# Push output to a dictionary
	letter_counts = {}
	for letter in required_letters:
		letter_counts[letter] = word.count(letter)

	# If there are not 0 counts, return True
	# If else, return False
	if 0 not in list(letter_counts.values()):
		print(True)
	else:
		print(False)
	
uses_all()
