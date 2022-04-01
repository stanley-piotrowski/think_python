#!/usr/bin/env python3

###################
#### middle.py ####
###################

# Take a list and return a new list that contains all but the first and last elements

# For example, the list below should produce the following:
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]

##############
#### Main ####
##############

def middle(input_list):
	middle_list = input_list[1:-1]
	print(middle_list)
