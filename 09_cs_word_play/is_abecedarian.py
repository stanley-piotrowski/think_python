#!/usr/bin/env python3

###########################
#### is_abecedarian.py ####
###########################

# This function reads in the words.txt file and checks to see if each word is an abecedarian-- that is, if all the letters are in alphabetical order
# If so, the function returns True for that word

# The function should return 596 words as True

# To arrive at the answer, type the following at the command line:;
# ./is_abecedarian.py | grep "True" | wc -l 
# Will return 596

##############
#### Main ####
##############

def is_abecedarian():

	# Create file handle and read input
	file_input = open("words.txt")
	
	# For each word, strip the newline character, push to a list
	# Create a new sorted list 
	# Compare the original list to the sorted one
	# If they match, return True; else, return False
	for line in file_input:
		word = list(line.strip("\n"))
		sorted_word = sorted(word)

		if word == sorted_word:
			print(True)
		else:
			print(False)

is_abecedarian() # returns 596 abecedarian words
