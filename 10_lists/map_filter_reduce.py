#!/usr/bin/env python3

##############################
#### map_filter_reduce.py ####
##############################

# Each of the sub-routines is an example of map, reduce, or filter using a toy list of fruits

# Define fruits
fruits = ['apple', 'banana', 'kiwi', 'orange', 'coconut', 'pear', 'strawberry', 'raspberry']

################
#### map.py ####
#################

# Capitalize each fruit in fruits, push the results to a new list, and print
print("\nMap result:")
upper_fruits = []
for fruit in fruits:
	upper_fruits.append(fruit.capitalize())

print(upper_fruits)

###################
#### filter.py ####
###################

# Filter to only include fruits that begin with 'a' or 's'
print("\nFilter results (starts with 'a' or 's'):")
filter_fruits = []
for fruit in fruits:
	if fruit.startswith('a') or fruit.startswith('s'):
		filter_fruits.append(fruit)

print(filter_fruits)

###################
#### reduce.py ####
###################

# Reduce elements of the list to a single value
# Create a new list of numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

print("\nReduce results: ")
for num in nums:
	total += num

print(total)