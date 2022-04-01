#!/usr/bin/env python3

##########################
#### most_frequent.py ####
##########################

# This function takes a string and prints the letters in decreasing order of frequency

# For example
# >>> s = 'aardvark'
# >>> most_frequent(s)
# 

##############
#### Main ####
##############

def most_frequent(s):

	d = {}
	for letter in s:
		if letter not in d.keys():
			d[letter] = 1
		else:
			d[letter] += 1

	# Sort the values in decreasing order, but only take the unique values
	sorted_values = sorted(list(set(d.values())), reverse = True)

	# Grab the keys corresponding to the following values
	for value in sorted_values:
		
		


