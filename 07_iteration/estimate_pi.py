#!/usr/bin/env python3

########################
#### estimate_pi.py ####
########################

# Exercise 7.3

# Use the formula from the textbook to compute and return an estimate of pi
# Use a while loop to compute the summation until the last term is smaller than 1e-15
# Use a similar approach to newtons_sqrt.py to print the result to the output

##############
#### Code ####
##############

# Calculate estimate of 1/pi
from math import inf


def estimate_pi():

	# Import modules and setup output to print
	import math
	print("k", "last term", "total", sep = "\t")
	print("-", "---------", "-----", sep = "\t")

	# Loop
	k = 1
	total = 0
	while k < inf:

		# Set starting variables of equation
		# note, to solve for pi, we need to reverse this
		term_01 = (2 * math.sqrt(2)) / 9801

		# Set values for last term	
		term_02_num = (math.factorial(4*k)) * (1103 + 26390 * k)
		term_02_denom = (math.factorial(k)**4) * (396**(4*k))

		# Evaluate expression
		last_term = term_02_num / term_02_denom
		term = term_01 * last_term
		total += term
		print(k, last_term, total, sep = "\t")

		# Increment k and the last term 
		k += 1
		
		if last_term < 1e-15:
			break

	# Multiply the first term and the final estimate of the last term
	return(1 / total)

# Note- this isnt done, finished getting the last term to within the level I want, but can't get the last part