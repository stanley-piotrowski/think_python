#!/usr/bin/env python3

###########################
#### has_duplicates.py ####
###########################

# Take a list and return True if there is an element that appears more than once

# Note, the function will not modify the original list

# For example:
# >>> t = [1, 2, 2, 3]
# >>> has_duplicates(t)
# True
# >>> t
# [1, 2, 2, 3] -- original list unmodified

# >>> t = ['apples', 'oranges', 'bananas']
# >>> has_duplicates(t)
# False
# >>> t
# ['apples', 'oranges', 'bananas] -- original list unmodified

##############
#### Main ####
##############

def has_duplicates(t):

	# Grab each unique element using a set converted to a list
	unique = list(set(t))

	# Build a dictionary of the element and the number of occurrences in the original list
	d = {}
	for i in unique:
		d[i] = t.count(i)

	# Loop over dictionary values-- if > 1, return False
	# Otherwise, continue
	for value in d.values():
		if value > 1:
			return True
		else:
			continue

	return False # if all are <= 1, there are no duplicates


