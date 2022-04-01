#!/usr/bin/env python3

####################
#### compare.py ####
####################

# Take two values, x and y, and return 1 if x > y, 0 if x == y, and -1 if x < y

# To run this function from the command-line, type the following:
# python3
# >>> from compare import compare
# >>> compare()
# The program will prompt the user to input an argument for x and y

# Compare function and take input from the user
def compare():
	x = input("Value of x (int): ")
	y = input("Value of y (int): ")

	# Re-assign variable types
	x = int(x)
	y = int(y)

	# Compare and return output
	if (x > y):
		return(1)
	elif (x < y):
		return(-1)
	else: 
		return(0)
