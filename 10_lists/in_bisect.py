#!/usr/bin/env python3

######################
#### in_bisect.py ####
######################

# This function takes the words.txt file, which is already sorted, and performs a bisection search-- first, split the file in half and check to see if the word is in the first half or the second half

 # This is similar to using the string.find() method using the 'in' operator

 # For each iteration, the function will return the bisection step and whether or not it has found the word

###############
 #### Main ####
 ##############

 def in_bisect(t):

	 f_input = open("words.txt")
	 t = []
	 for line in f_input:
		t.append(line.strip("\n"))