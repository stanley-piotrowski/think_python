#!/usr/bin/env python3

#####################
#### has_no_e.py ####
#####################

# This program reads through words.txt and prints only the words that have no 'e' 
# In addition, it will compute the percentage of words in the list that have no 'e'

##############
#### Main ####
##############

def has_no_e():

	# Create file handle
	f_input = open("words.txt")

	# Count words with e's and those without
	with_e = 0
	without_e = 0
	
	# Loop
	for line in f_input:
		word = line.strip("\n")

		if word.count("e") == 0:
			print(word)
			with_e += 1
		else:
			without_e += 1

	print("Number with e's:", with_e)
	print("Number without e's:", without_e)

	perc_without_e = round(without_e / (with_e + without_e) * 100, 	ndigits = 2)
	print("Percentage of words without e's: ", perc_without_e, "%", sep = "")
	
has_no_e()
