#!/usr/bin/env python3
import sys
import json
import random as r


# function to check if the two heads are the same
def check_animals(animal_1, animal_2):
	if animal_1.get('head') == animal_2.get('head'):
		return False
	else:
		return True

def change_animals(animal_1, animal_2):
	# need to make sure animals.json is open
	with open(sys.argv[1], 'r') as f:
		data = json.load(f)
		
		# in the off-chance that all 19 animals have the same head, we'll use
		# a count variable to ensure we don't have an infinite loop
		# for the sake of ease, just going to try no more than 25 combinations of
		# animals (assumes some animals will be drawn twice)
		count = 0
		while not check_animals(animal_1, animal_2) and count < 25:
			animal_2 = data['animals'][r.randint(0,19)]
			count += 1
	return animal_2
def main():
	# read from animals.json
	with open(sys.argv[1], 'r') as f:
		data = json.load(f)
		
		# get two animals, if their heads are the same, get another second animal
		animal_1 = data['animals'][r.randint(0,19)]
		animal_2 = data['animals'][r.randint(0,19)]
		
		# run checkanimals function
		animal_2 = change_animals(animal_1, animal_2)
		print(animal_1)
		print(animal_2)

if __name__ == '__main__':
	main()
