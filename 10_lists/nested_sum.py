#!/usr/bin/env python3

#######################
#### nested_sum.py ####
#######################

# Given a nested list of integers, return the total sum
# For example, given the following nested list:
# t = [[1, 2], [3], [4, 5, 6]]
# nested_sum(t)
# 21

##############
#### Main ####
##############

def nested_sum(int_list):

	# Loop to get the nested sums
	total = 0
	for ints in int_list:
		total += sum(ints)

	print(total)