#!/usr/bin/env python3
import sys
import unittest
from read_animals import check_animals

class TestReadAnim(unittest.TestCase):
	
	def test_check_animals(self):
		# create some animals to test
		animal_1 = {'head': 'bull', 'body': 'yak-sole', 'arms': 4, 'legs': 6, 'tail': 10}
		animal_2 = {'head': 'bull', 'body': 'horse-pup', 'arms': 2, 'legs': 9, 'tail': 11}
		animal_3 = {'head': 'snake', 'body': 'toucan-weasel', 'arms': 6, 'legs': 3, 'tail': 9}
		
		# test these animals with the unittester
		self.assertEqual(check_animals(animal_1, animal_2), False)
		self.assertEqual(check_animals(animal_1, animal_3), True)
		self.assertEqual(check_animals(animal_2, animal_3), True)

if __name__ == '__main__':
	unittest.main()
		
