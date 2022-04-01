#!/usr/bin/env python3

######################
#### Exercise 9.7 ####
######################

# This function searches through the words_subset.txt file and searches for words that have three consecutive pairs of letters
# To create the file, I subsetted 10 lines from the words.txt file and added a few words with three consecutive pairs of letters-- bookeeper and bookkeepers

##############
#### Main ####
##############

def ex_9_7():

	# Create file input and read contents
	file_input = open("words_subset.txt")

	# Create empty dictionary to hold the words and number of consecutive pairs of letters
	consecutive_dict = {} 

	# Loop through each word
	# Push the words as dictionary keys
	# Loop through each key and look ahead one index
	# If the strings match, add one to the counter
	# Push the final tally of the counter to the dict values
	for line in file_input:
		word = line.strip("\n")
		double_counter = 0
		for i in range (0, len(word)):
			if i + 1 < len(word):
				if word[i] == word[i + 1]:
					double_counter += 1
		consecutive_dict[word] = double_counter

	# Loop through the dictionary balues
	# If values > 3, print the word
	for key, value in consecutive_dict.items():
		if value >= 3:
			print(key)

ex_9_7() # returns only bookkeeper and bookeepers
				
			
