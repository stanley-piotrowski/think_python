#!/usr/bin/env python3

####################
#### sandbox.py ####
####################

# Build a simple dictionary mapping numbers in English to Spanish
eng = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

sp = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez']

eng2sp = {}
for i, j in zip(eng, sp):
	eng2sp[i] = j

print(eng2sp)

# Loop through all of the keys and values separately
for key in eng2sp.keys():
	print(key)

for value in eng2sp.values():
	print(value)

# Create a letter counter
# We create the empty dictionary and traverse the string
# If the letter is not in the dictionary, we create a new key and bind the value of 1 to the key
# If the letter is already in the dictionary, we increment the value by one
dino = "brontosaurus"
d = {}
for letter in dino:
	if letter not in d:
		d[letter] = 1
	else:
		d[letter] += 1
	
print(d)

# Alternatively, we could do the same thing in a few more steps using a set, which just takes the unique values
unique = "".join(list(set(dino)))
d2 = {}
for letter in unique:
	d2[letter] = dino.count(letter)

print(d2)

sorted(d.items()) == sorted(d2.items()) # returns True

# Create a dictionary another way
mlb_team = dict(
	colorado = 'rockies',
	boston = 'red sox', 
	minnesota = 'twins', 
	milwaukee = 'brewers', 
	seattle = 'mariners'
)

# Python preserves the order of the dictionary based on how it was created
# If you want to print the dictionary contents in sorted order, you can create a variable of the sorted keys, then grab the associated values
sorted_teams = sorted(mlb_team.keys())
for team in sorted_teams:
	print(mlb_team[team])
