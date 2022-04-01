#!/usr/bin/env python3

# Chapter 02: Variables, expressions, and statements

#####################################################################
#### Notes ####
#####################################################################

# State diagram- drawing an arrow from a variable name to its value
# There are many keywords that the Python interpreter uses to understand the structure of the program; these keywords can't be used as variable names
# An example of one of the keywords is 'class' 
# In Python lingo, an expression is a combination of values, variables, and operators to produce some output
# A statement is some code that has an effect (e.g., 'print(17)' prints the number 17)
# Importantly, in script mode (i.e., running a Python script on the command line as opposed to running Python interactively), results of expressions don't print to the screen; you need a 'print()' statement for that.
# Python follows the PEMDAS order of operations

# Strings ----
# You can't perform operations on any strings, except for adding and multiplying
# An example of adding and multipling string variables is shown below
string = 'chinese_food'
string_add = string + string + string
string_mult = string*3
print("Strings added together: ", string_add)
print("Strings multiplied together: ", string_mult) # gives the same result as the statement above

# Debugging -----
# Syntax errors occur when there is an issue with the structure of the program (e.g., missing closing parentheses in an expression or statement)
# Runtime errors occur after the program has started running (i.e., there generally isn't an issue with the syntax, or structure, of the program)
# Semantic errors occur when the program runs without any error, but doesn't produce the intended output- instead, it produces something else, but it's sometimes difficult to figure out what that is because you need to work backwards and look at the output from a program

###############################################################################
#### Exercises ####
###############################################################################

# 2.1) ----
# 1) 42 = n is not legal, because variable names cannot start with numbers; you will get a syntax error
# 2) y = x = 1 is legal- both 'x' and 'y' will both have the value 1 assigned to them
# 3) If you put a ';' at the end of a Python statement, nothing happens (at least not in Python3)
# 4) If you put a '.' at the end of a Python statement, however, you'll get a syntax error (i.e., there's something wrong with the structure of the program)
# 5) If you try multiplying two variables together like that in Python, you'll get a 'NameError' because 'xy' is not defined, but 'x' and 'y' individually are

# 2.2) ----
# 1) The volume of a sphere with a radius of 5 is approximately 532.3 (the value of pi was defined as 3.14)
# 2) Here's the structure of how I wrote this out in the interactive mode:

cover_price = 24.95
discount_price = cover_price - (24.95*0.4) # take off 40% discount for the bookstore 

# At this point, the cost of a book (without shipping) is approximately $14.97 
# We know it's $3 for the first copy (1/60 copies), and $0.75 for each additional copy (59/60)
# Price for first copy is $17.97 ($3 shipping)
# Now we need to get the shipping costs for 59 copies
first_copy = discount_price + 3# $17.97
shipping_costs_regular = 0.75*59 # $44.25

# Now we need to get the total cost of the remaining 59 copies
book_cost_regular = 59*14.97 # equals approximately $ 883.23

# Now add the costs of the books with the reduced shipping and the cost of the first book shipment
print("The total wholesale cost for 60 copies is: $", first_copy + book_cost_regular, sep = "")

# 3) Here is the breakdown of statements and expressions for this exercise

# Run 1 mile at an easy pace
first_mile = 8.15

# Run 3 miles at a different tempo
fast_pace = 7.12 * 3

# Run one more mile at an easy pace
total_run_time = first_mile + fast_pace + first_mile

# Total runtime is 37.66, which is 38 minutes and 6 seconds
# So, if he left the house at 6:52, he'd be home by 7:30am for breakfast 

