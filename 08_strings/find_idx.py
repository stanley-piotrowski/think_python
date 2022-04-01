#!/usr/bin/env python3

# Take three arguments: word, letter, and index, all as input from the command line
# Search through the word, starting at a specified index, and if the string at word[index] == letter, return the index
def find_idx():

	# Parse arguments
	word = str(input("Word: "))
	letter = str(input("Letter: "))
	index = int(input("Starting index: "))

	# Search for the letter and return the index
	index = index 
	while index < len(word):
		if word[index] == letter:
			return(index)
		index += 1
	
	# If the letter isn't detected, return -1 by default
	return(-1)

find_idx()

