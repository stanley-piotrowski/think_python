#!/usr/bin/env python3

###################
#### avoids.py ####
###################

# This program takes a string of forbidden letters as input and prints the number of words that don't contain any of them

##############
#### Main ####
##############

def avoids():

	# Parse user input and create file handle
	blacklist = str(input("Forbidden letters: "))
	file_input = open("words.txt")

	# Check that the blacklist input is 5 letters
	while len(blacklist) != 5:
		blacklist = str(input("Please input 5 forbidden letters: "))

	# Loop through each word in the file handle
	# Loop through each blacklist letter 
	for line in file_input:
		word = line.strip("\n")
		blacklist_counter = 0
		for letter in blacklist:
			if word.count(letter) != 0:
				blacklist_counter += 1
		if blacklist_counter == 0:
			print(word)

avoids()