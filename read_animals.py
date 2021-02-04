import json
import random as r

if __name__ == '__main__':
	with open('animals.json', 'r') as f:
		data = json.load(f)
		print(data['animals'][r.randint(0,19)])
