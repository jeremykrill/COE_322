import petname as p
import random as r
import json

def generate():
	types = ["snake", "bull", "lion", "raven", "bunny"]

	data = {}
	data['animals'] = []

	for i in range(20):
		arm = r.randint(2,10)
		leg = r.randint(3,12)
		tails = arm + leg

		data['animals'].append({
		"head": types[r.randint(0,4)],
		"body": p.name() + "-" + p.name(),
		"arms": arm,
		"legs": leg,
		"tail": tails
	})
	return data

def main():
	data = generate()
	with open('animals.json', 'w') as f:
		json.dump(data, f)

if __name__ == '__main__':	
	main()
