#!/usr/bin/env python3

######################
#### Exercise 9.1 ####
######################

# This program will read words.txt and print out only the words with more than 20 characters (not including whitespaces)

def print_subset():

	# Create file handle
	f_input = open("words.txt")

	# For loop to print words
	for line in f_input:
		word = line.strip("\n")
		#print(word, " (", len(word), ")", sep = "")
		if len(word) > 20:
			print("Word: ", word, ", length: ", len(word), 
			sep = "")

print_subset() 
	
