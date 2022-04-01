#!/usr/bin/env python3

# Chapter 03: Functions

######################################################################################################
#### Notes ####
######################################################################################################

# A module is a file that contains a collection of related functions, like a library in R
# We can import the 'math' module below
import math
from os import WIFEXITED

# When calling a function from a specific module, we need to use dot-notation
# For example, let's call the sin() function from math
radians = 0.7
height = math.sin(radians)
print(height)

# To create a new function, we'll use the keyword 'def' to indicate that we're defining a new function
def lyrics():
    print("I'm a lumberjack and I'm okay")
    print("I sleep all night and I work all day")

# Now call the function
lyrics()

# Functions can be used inside other function calls
def repeat_lyrics():
    lyrics()
    lyrics()

# Call the function again
repeat_lyrics()

# The scope of variables within function calls is important to consider- the variables only exist within the function, so they cannot be acccessed by other functions outside of it
# Similarly, parameters are also local- parameters for function definitions are not defined and able to be accessed globally outside of the function

# Stack diagrams show which variables and parameters belong to which function, and which function calls which
# So, if there's an error in a sequence where several functions have called each other, Python will print a sort of stack error diagram, showing the function and its arguments, all the way up the chain to the '__main__' function
# This is also called a 'traceback' to help walk back to where the error occured, because the way the functions are printed in the traceback is the same order as they appear in the stack diagram

# Functions are useful because it reduces the amount of repetitive code so that if you need to change something, you only need to do it in one place, not across a program
# Additionally, once a function is working properly, it can be called and used in other programs

######################################################################################################
#### Exercises ####
######################################################################################################

# 3.1) ----
# Write a function named 'right_justify()' that takes a string named 's' as an argument and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display

# General ideas and pseudocode:
# Get the length of the string using 'len()'
# 
def right_justify(s):
    num_spaces = 70 - len(s)
    print(num_spaces * " ", s)

right_justify('monty')

# 3.2 ----
# Below is the example script for 'do_twice()', which takes one argument, 'f' 
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)

# Modify 'do_twice()' to take a function object 'f' and a value as an argument, in addition to 'reps'
def do_twice(f, reps, arg):
    for i in range(0, reps):
        f(arg)

def print_twice(bruce):
    print(bruce)
    print(bruce)

print("Modified do_twice() function:")
do_twice(f = print_twice, reps = 2, arg = "spam")

# Define a new function 'do_four()' with only two statements in the body of the function
def do_four(f, arg):
    for i in range(0, 4):
        f(arg)

def print_whatever_arg(string):
    print(string)

print("\ndo_four() exercise:")
do_four(print_whatever_arg, "The Lord of the Rings")

# 3.3) ----
# Write a function that draws a grid using only the values we've learned so far
print("\n")
def print_box(width_spaces, length_spaces):

    # Define how horizontal and vertical edges should look
    horizontal = "-" + " "
    vertical = "|"

    # Define the length and width of the edges
    horizontal_line = horizontal * width_spaces
    vertical_line = vertical * length_spaces

    # Put horizontal and vertical lines together into two variables
    horizontal_lines = "+ " + horizontal_line + "+ " + horizontal_line + "+"
    vertical_lines = vertical_line + "\n" + "+" + "\n" + vertical_line + "\n" + "+"

    # Create outer and inner lines
    top_line = "+ " + horizontal_line + "+ " + horizontal_line + "+ "
    second_line = "\n" + vertical + (" " * (width_spaces * 2 + 1)) + vertical + (" " * (width_spaces * 2 + 1)) + vertical + "\n" # end on a new line to start next part of the square

    print(top_line)
    print(second_line * width_spaces)
    print(top_line)
    print(second_line * width_spaces) 
    print(top_line)

# Call the function with the same length and width as the textbook 
print_box(width_spaces=4, length_spaces=4)
print_box(width_spaces=10, length_spaces=10)
