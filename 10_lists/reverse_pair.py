#!/usr/bin/env python3

#######################
#### is_reverse.py ####
#######################

# This program finds all of the reverse pairs of words in the words.txt file

"""
The current version of the program proceeds more by brute force using the following steps:
1) Read the contents of the file and push each word into a list
2) For each word in the list, reverse the string and push the contents to a new reverse list
3) Traverse the reverse list and if the reverse word is in the original list, print the string from the original list
"""

##############
#### Main ####
##############

def is_reverse():

	f_input = open("words.txt")

	# Push each word to a list
	t = []
	for line in f_input:
		t.append(line.strip("\n"))

	# Create a new list of each word reversed
	rev_list = []

	for word in t:
		rev = []
		for i in range(-1, -(len(word) + 1), -1):
			rev.append(word[i])
		rev = "".join(rev)
		rev_list.append(rev)
	
	# Traverse the reversed word list and print the member of the reversed pair from the original list
	for rev_word in rev_list:
		if rev_word in t:
			idx = t.index(rev_word)
			print(t[idx])
		else: 
			continue

is_reverse()
	
			


	
