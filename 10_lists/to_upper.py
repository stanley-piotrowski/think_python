#!/usr/bin/env python3

#####################
#### to_upper.py ####
#####################

# Take a string as input and capitlize each letter

###############
#### Main #####
###############

def to_upper():

	input_string = str(input("string: "))

	s_list = []
	for letter in list(input_string):
		s_list.append(letter.capitalize())
	
	out = "".join(s_list)
	print(out)

to_upper()

