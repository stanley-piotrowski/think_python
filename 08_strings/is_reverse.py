#!/usr/bin/python3 

def is_reverse():

	# Parse input
	word1 = str(input("Word #1: "))
	word2 = str(input("Word #2: "))

	# Traverse each word and check if word 1 is the reverse of word 2
	i = 0
	j = len(word2) - 1

	# If the first letter and last letter don't match, FALSE
	if word1[i] != word2[j]:
		return(False)
		
	for i in range(0, len(word1)):
		# print("i: ", i, "j: ", j)
		if word1[i] != word2[j]:
			return(False)
		i += 1
		j -= 1
	
	return(True)
	