#!/usr/bin/env python3

#####################
#### distance.py ####
#####################

# Take four coordinates- two x-coordinates and two y-coordinates- and return the distance between them using the pythagorean theorem

# To run this function, type the following at the command-line
# python3
# >>> from distance import distance
# >>> distance()

# Function
def distance():

	# Parse input
	x1 = int(input("x1 coordinate (int): "))
	y1 = int(input("y1 coordinate (int): "))
	x2 = int(input("x2 coordinate (int): "))
	y2 = int(input("y2 coordinate (int): "))

	# Calculate distance
	import math
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)

	return(result)
	