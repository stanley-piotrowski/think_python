#!/usr/bin/env python3

##########################
#### countdown_ex2.py ####
##########################

# While n > 0, print n and then subtract 1 from n
# When n == 0, print "Blastoff!"

# Function
def countdown():

	# Get input from user
	n = int(input("n: "))

	# While loop
	while (n > 0):
		print(n)
		n = n -1
	print("Blastoff!")

