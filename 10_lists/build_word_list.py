#!/usr/bin/env python3

############################
#### build_word_list.py ####
############################

# Read the words.txt file and push to a list such that each word is an element of the list

# There are two versions-- one using the list.append() method, and the other using the idiom list = list + [element]

# Note, the second version will take substantially longer because it needs to copy the contents of the list from the previous generation, add the new word, and then create a new binding-- effectively creating a new list each iteration

# The first version only needs to modify the existing list

##############
#### Main ####
##############

def build_word_list_append():

	f_input = open("words.txt")
	word_list = []
	for line in f_input:
		word_list.append(line.strip("\n"))

	print(word_list)

def build_word_list_copy():

	f_input = open("words.txt")
	word_list = []
	for line in f_input:
		word_list = word_list + [line]
	
	print(word_list)