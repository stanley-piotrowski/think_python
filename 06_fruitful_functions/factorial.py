#!/usr/bin/python3

######################
#### factorial.py ####
######################

# Given some input, n, return n!

# Function
def factorial():

	# Parse input
	n = int(input("n: "))

	# Calculate n!
	n_factorial = n
	if (n == 0):
		return(1)
	else:
		while (n > 0):
			n_factorial = n_factorial * (n - 1)
			n = n - 1
			if (n - 1 == 0):
				return(n_factorial)
		return(n_factorial)
	