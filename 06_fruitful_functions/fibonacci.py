#!/usr/bin/env python3

######################
#### fibonnaci.py ####
######################

# Take a number as input, n, and return the fibonacci sequence, such that:
# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)

# Function
def fibonacci(n):

	# While loop
	fibonacci_list = []
	if (n == 0):
		return(0)
	elif (n == 1):
		return(1)
	else:
		return(fibonacci(n - 1) + fibonacci(n - 2))
