#!usr/bin/env python3

def count_counter():

	# Take arguments as input
	word = str(input("Word: "))
	letter = str(input("Letter: "))

	# Count the number of occurrences of 'letter' in 'word'
	counter = 0
	for i in range(0, len(word)):
		if word[i] == letter:
			counter += 1
	
	return(counter)