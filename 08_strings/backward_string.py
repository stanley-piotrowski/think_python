#!/usr/bin/env python3

############################
#### backward_string.py ####
############################

# Print each word of a string provided by the user backwards

# Function
def backward_string():

	# Parse input
	string = input("String: ")

	# Loop
	for i in range(-1, -(len(string) + 1), -1):
		print(string[i])

# Call function
backward_string()