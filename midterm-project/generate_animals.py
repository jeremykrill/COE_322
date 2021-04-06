#!/usr/bin/env python3
import sys
import petname as p
import random as r
import json
import uuid
import datetime
import redis

# create a generate function to generate our animals
def main():
	types = ["snake", "bull", "lion", "raven", "bunny"]

	# data variable to hold animals
	data = {}
	data['animals'] = []

	for i in range(20):
		# randomly generate arm and leg variables
		arm = r.randint(2,10)
		while(arm % 2 != 0):
			arm = r.randint(2,10)
		leg = r.randint(3,12)
		while(leg % 3 != 0):
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
		"tail": tails,
		"uid": str(uuid.uuid4()),
		"created_on": str(datetime.datetime.now())
		})
	rd = redis.StrictRedis(host='krilljs-redis', port=6396, db=0)
	rd.set('animals', json.dumps(data, indent=2))

if __name__ == '__main__':
	main()
