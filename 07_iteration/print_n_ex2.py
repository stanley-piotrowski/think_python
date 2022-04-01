#!/usr/bin/python3

########################
#### print_n_ex2.py ####
########################

# This function performs the same operations as print_n() from chapter 5 but uses a loop instead of recursion

# Function- print a string "s" "n" times
def print_n():
	
	# Get input from user
	n = int(input("n: "))
	s = input("s: ")

	# Loop
	while (n > 0):
		print(s)
		n = n - 1
	return

