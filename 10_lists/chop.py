#!/usr/bin/env python3

#################
#### chop.py ####
#################

# Take a list, modify it by removing the first and last elements, and return None

# For example:
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t 
# [2, 3] --> demonstrates that chop() modified the list

##############
#### Main ####
##############

def chop(t):
	t.pop(0)
	t.pop(-1)


