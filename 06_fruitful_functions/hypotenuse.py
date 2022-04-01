#!/usr/bin/env python3

#######################
#### hypotenuse.py ####
#######################

# Take two integers as input and calculate the hypotenuse of a right triangle, then return the result

# To run this program, type the following in the command line:
# python3
# >>> from hypotenuse import hypotenuse
# >>> hypotenuse()

# Function
def hypotenuse():

	# Parse input
	x = int(input("Side #1 length (int): "))
	y = int(input("Side #2 length (int): "))

	# Calculate hypotenuse
	import math
	result = math.sqrt(x**2 + y**2)
	
	return(result)