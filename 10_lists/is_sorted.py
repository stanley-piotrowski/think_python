#!/usr/bin/env python3

######################
#### is_sorted.py ####
######################

# Take a list and return True if it is sorted in ascending order and False otherwise

# For example:
# >>> is_sorted([1, 2, 3])
# True
# >>> is_sorted(['b', 'a'])
# False

##############
#### Main ####
##############

def is_sorted(t):
	if t == sorted(t):
		return True
	else: 
		return False

