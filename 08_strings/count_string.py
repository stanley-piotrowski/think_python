#!/usr/bin/env python3

#########################
#### count_string.py ####
#########################

# Exercise 8.3

# This is a function which performs the same task as the .count() method

# Code
def count_string():

    # Parse input
    string = input("String: ")
    substring = input("Substring to count: ")

    # Count number of occurrences of the substring in string
    count = 0
    j = len(substring)

    for i in range(0, len(string)):
        if string[i:j] == substring:
            count += 1
        i += 1
        j += 1

    print(substring.upper(), " occurs in ",
          string.upper(), " ", count, " times",
          sep = "")


# Test on banana
count_string()
