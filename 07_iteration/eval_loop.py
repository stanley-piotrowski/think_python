#!/usr/bin/env python3

######################
#### eval_loop.py ####
######################

# Exercise 7.2 

# Iteratively prompt the user, take the resulting input, and evaluate it with eval(), print the result, and continue until the user enters "done"
# When the user enters "done", print the last expression evaluated

##############
#### Code ####
##############

# Function
def eval_loop():

	# Loop and parse input from user
	while True:
		string = str(input("String to evaluate: "))
		if string == "done":
			return(result)
		else:
			result = eval(string)
			print(result)
	