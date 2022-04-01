#!/usr/bin/env python3

######################
#### ackermann.py ####
######################

# This is exercise 6.2- the Ackermann function

# The Ackermann function is defined as follows
# A(m,n)
# if m = 0 --> n + 1
# if m > 0 and n = 0 --> A(m - 1, 1)
# if m > 0 and n > 0 --> A(m - 1, A(m, n - 1))


# Function
def ackermann(m, n):

	if (m == 0):
		n = n + 1
	
	elif (m > 0 and n == 0):
		ackermann(m - 1, 1)
	
	elif (m > 0 and n > 0):
		return(ackermann(m - 1, ackermann(m, n - 1)))