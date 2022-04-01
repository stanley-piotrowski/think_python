#!/usr/bin/env python3

####################
#### sandbox.py ####
####################

# Tuple assignment is more convenient and compact code
# We could generate both the username and domain for the email address below using different implementations
# But, tuple assignment is much quicker to type
address = "monty@python.org"
username, domain = address.split("@")

# Return values
# >>> username
# 'monty'
# >>> domain
# 'python.org'

# Now using the long way-- for example, splitting into a list and extracting the elements by their index
username = address.split("@")[0] # returns 'monty'
domain = address.split("@")[1] # returns 'python.org'
print(username, domain)

# Create a function called 'sum_all()' that takes any number of arguments and returns their sum
# This is an example of scattering the contents of a tuple as multiple arguments to a built-in function
def sum_all(*nums):
	return sum(*nums)

nums = (1, 2, 3) # tuple
sum_all(nums) # returns 6 correctly

# Instead of using the built-in zip() function, you could also use enumerate
for index, element in enumerate("abc"):
	print(index, element)

# More tutorials from intermediate python 
mylist = ['apple', 'banana', 'cherry']
print(mylist)
mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")

# Sort and reverse methods-- modify the existing list
mylist.sort()
mylist.reverse()

# Instead, use the sorted() or functions, which create a new list
sorted(mylist)
mylist = [0] * 5
mylist = list(range(1, 11))
mylist[1::2] # uses the step index
mylist[::-1]
mylist_cpy = mylist.copy() # creates a new list 

# If you use the following idiom
# mylist_cpy = mylist
# Both objects are referencing the same list in memory-- so, if you change the original list, the copy gets modified
# In order to actually create a copy, you can use the copy() method

# List comprehension-- more succinct ways of writing a for loop 
# For example, square every element of the following list
a = list(range(1, 7))

# Here's the long way to do it
b = []
for i in a:
	b.append(i*i)
b

# Now with list comprehension
[i*i for i in a] == b # returns True

# Tuples-- immutable, often used for objects that belong together
# A few ways to create a tuple
mytuple = ('max', 28, 'boston')
mytuple = tuple(['max', 28, 'boston'])

item = mytuple[0]
[i for i in mytuple] # quick way to print all elements of a tuple
x = 'max'
for i in mytuple:
	if i == x:
		print('match')
	else:
		print('nomatch')

# Tuple assignment-- unpacking
mytuple
name, age, city = mytuple

# Comparing the size of lists and tuples with the same elements
a = ['lion', 'tiger', 'bear', 'koala']
b = tuple(a)
import sys
sys.getsizeof(a) # 120 bytes
sys.getsizeof(b) # 72 bytes

# Dictionaries






