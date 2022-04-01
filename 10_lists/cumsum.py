#!/usr/bin/env python3

###################
#### cumsum.py ####
###################

# Given a list of integers, return a new list with the cumulative sums
# For example, given the following list:
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]

##############
#### Main ####
##############

def cumsum(int_list):

	cumsum_list = []
	cumsum_list.append(int_list[0]) # add the first element
	print(cumsum_list)

	for i in len(int_list):
		cumsum_list.append(sum(int_list[i] + int_list[i + 1]))
	
	print(cumsum_list)

