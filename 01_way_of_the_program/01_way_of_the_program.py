#!/usr/bin/env python3

# Import modules
import sys

########################################################################
#### Notes #### 
########################################################################
# Print first hello world
print("hello, world!\n")

# Important to note the type() function to check the type of an object
# For example, a string
s = "This is a string"
print("The string is of type:", type(s))

########################################################################
#### Exercises #### 
########################################################################
# 1.1) 
# 1) In a print statement, what happens if you leave out one of the parentheses, or both?

# Leaving out one of the parentheses
# print "hello world!" -- won't run, syntax error

# 2) If you are trying to print a string, what happens if you leave out one of the quotation marks?

# Leaving out one of the quotation marks also results in a syntax error

# 3) What happens if you put a plus sign before a number?  

# What about 2++2?
print(2++2) # returns 4, so nothing weird happens

# 4) What happens if you try to put leading zeros in front of a number?
# For example, 011?
# print(011) -- returns a syntax error, 'leading zeros in decimal integer literals are not permitted'

# 5) What happens if you have two values with no operator between them?
# print(5 5) -- returns a syntax error, 'invalid syntax'

# 1.2) Using the Python interpreter as a calculator
# 1) How many seconds are there in 42 minutes 42 seconds
seconds = (42*60) + 42
print("There are %d seconds in 42 minutes 42 seconds.\n" % seconds)

# 2) How many miles are there in 10 kilometers (there are 1.61 kilometers in 1 mile)
miles = 10/1.61
print("There are %f miles (full decimal) in 10 kilometers.\n" % miles)
print("There are %d miles (rounded to nearest integer) in 10 kilometers.\n" % miles)

# 3) If you run a 10 km race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and secodns?)  What is your average speed in miles per hour?

# Calculate miles and total number of seconds
miles = 10/1.61
seconds = (42*60) + 42

# Calculate average time in seconds
avg_time_seconds = miles/seconds # 0.002 miles per second
print("The average page is %f miles per second.\n" % avg_time_seconds)



