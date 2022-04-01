#!/usr/bin/env python3

#########################
#### newtons_sqrt.py ####
#########################

# Calculate the square root using Newton's method iteratively

# Use a while loop with the condition "True" until the result (y) == x and keep track of the number of iterations used to get the answer
def newtons_sqrt():

	# Parse input
	a = int(input("Number to calculate sqrt of: "))
	x = int(input("First estimate of sqrt root (less than x): "))

	# Checks
	if not x < a:
		return("Error: initial estimate of 'x' must be less than 'a'")

	# Print header info
	print("a", "newtons_sqrt(a)", "math.sqrt(a)", "diff", sep = "\t")
	print("-", "--------------", "------------", "----", sep = "\t")

	# Function
	import math
	while True:
		
		# Set equality threshold
		epsilon = 0.0000001

		# Initial calculation
		y = (x + a/x) / 2
		diff = y - math.sqrt(a)

		# Print results
		print(float(a), "\t", y, "\t", math.sqrt(a), "\t", diff)

		# If estimate == output, break out of the loop
		if abs(y - x) < epsilon:
			break
		else:
			x = y
	
	return(x)


		