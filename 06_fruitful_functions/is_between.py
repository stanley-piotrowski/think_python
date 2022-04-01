#!/usr/bin/env python3

#######################
#### is_between.py ####
#######################

# Parse three integers from the user as input and return True if x <= y  <= z or False otherwise

# From the command line, type the following:
# python3
# >>> from is_between import is_between
# >>> is_between()

# Function
def is_between():

	# Parse input
	x = int(input("x: "))
	y = int(input("y: "))
	z = int(input("z: "))

	# Compare
	return(x <= y <= z)