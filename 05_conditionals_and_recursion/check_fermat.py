#!/usr/bin/python3

#############
#### 5.2 ####
#############

# Check Fermat's theorem and take four prompts as input from the user

# Parse input from the user
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("a", type = int)
parser.add_argument("b", type = int)
parser.add_argument("c", type = str)
parser.add_argument("n", type = int)

args = parser.parse_args()
a = int(args.a)
b = int(args.b)
c = int(args.c)
n = int(args.n)

# Check theorem
x = a ** n
y = b ** n
z = c ** n

if ((args.n > 2) and (x + y == z)):
	print("Holy smokes, Fermat was wrong!")
else:
	print("No, that doesn't work.")
