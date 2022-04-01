#!/usr/bin/env python3

######################
#### word_dict.py ####
######################

# Read contents of the words.txt file and sotre each word as a key in a dictionary
# This is an efficient way of checking to see if user-provided strings are in a dictionary

##############
#### Main ####
##############

def word_dict():

	f_input = open("words.txt")
	d = {}
	for line in f_input:
		d[line.strip("\n")] = ""

	# Create an inverted dictionary 
	# Each key is a frequency; each value is a list of letters with that frequency
	freq_dict = {}
	for key in d:
		value = d[key]
		if value not in freq_dict:
			freq_dict[value] = [key]
		else:
			freq_dict[value].append(key)

