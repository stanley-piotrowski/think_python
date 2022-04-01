#!/usr/bin/env python3

##########################
#### check_strings.py ####
##########################

"""
Given two strings as input, test if the
 second string is a reverse of the first
"""

# Code
def check_strings():

    # Parse input
    string1 = input("String #1: ")
    string2 = input("String #2: ")

    # Loop over both strings
    i = 0
    j = len(string2) - 1

    while j > -1:
        print(i, " string #1, ", string1[i].lower(), sep = "")
        print(j, " string #2, ", string2[j].lower(), sep = "")

        # Increment
        i += 1
        j -= 1

# Test
check_strings()

# Note, in the book, we need to change the program
# We can do that by modifying the while loop so that the condition it checks is if j > -1
# This will ensure that the 0th index is included in the loop