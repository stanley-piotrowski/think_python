#!/usr/bin/env python3

#######################
#### is_anagram.py ####
#######################

# Given two strings, if you can rearrange the letters from one to spell the other, they are anagrams

# If they are anagrams, return True; otherwise, return False

# Note, whitespace and capitalization are ignored

# For example:
# >>> a = 'I am Lord Voldemort'
# >>> b = 'Tom Marvolo Riddle'
# >>> is_anagram(a, b)
# True

##############
#### Main ####
##############

def is_anagram(string1, string2):

	# Replace spaces and convert all to lowercase 
	string1 = "".join(sorted(string1.replace(" ", "").lower()))
	string2 = sorted(string2.replace(" ", "").lower())

	# Zip and compare
	for i, j in zip(string1, string2):
		if i != j:
			return False
		else: 
			continue # if they don't break, continue
	
	return True # if it doesn't break, they're anagrams 

