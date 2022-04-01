#!/usr/bin/env python3 

#############
#### 5.3 ####
#############

# Take three integers as arguments and print "Yes" if you can make a triangle and "No" if you can't

# If any of the three stick lengths is greater than the sum of the other two, then you cannot form a triangle

# Parse stick lengths from the user
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type = int, help = "Length of side 1")
parser.add_argument("y", type = int, help = "Length of side 2")
parser.add_argument("z", type =	int, help = "Length of side 3")

# Re-assign variables
args = parser.parse_args()
x = args.x
y = args.y
z = args.z

# Define possibilities
if (x > (y + z) or y > (x + z) or z > (x + y)):
	print("No")
else:
	print("Yes")
