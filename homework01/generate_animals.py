import petname as p
import random as r
import json

# create a generate function to generate our animals
def generate():
	types = ["snake", "bull", "lion", "raven", "bunny"]

	# data variable to hold animals
	data = {}
	data['animals'] = []

	for i in range(20):
		# randomly generate arm and leg variables
		arm = r.randint(2,10)
		leg = r.randint(3,12)
		# sum arms and legs to find tails
		tails = arm + leg
	
		# append new animal to data
		data['animals'].append({
		"head": types[r.randint(0,4)],
		# use name method from petname to create body
		"body": p.name() + '-'+ p.name(),
		"arms": arm,
		"legs": leg,
		"tail": tails
	})
	# return data as the output
	return data

# main function
def main():
	data = generate()
	# write to new json file, animals.json
	with open('animals.json', 'w') as f:
		json.dump(data, f)

if __name__ == '__main__':
	main()
