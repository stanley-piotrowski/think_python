#!/usr/bin/env python3

#########################
#### 5.4- recurse.py ####
#########################

# Recursive function demonstration

# Note- this needs to be updated to accept arguments from the command-line 

# Parse arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("n", type = int)
parser.add_argument("s", type = int)

# Execute parser
args = parser.parse_args()
 
# Recurse
def recurse(n, s):
	print("n = ", n, sep = "")
	print("s = ", s, sep = "")
	if n == 0:
		print(s)
	else:
		recurse(n-1, n+s)
