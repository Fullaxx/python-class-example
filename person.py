#!/usr/bin/env python3

class Person:
#	Class variable shared by all instances
	species = 'Human'
	def __init__(self, inc_name, inc_age):
#		Instance variable unique to each instance
		self.name = inc_name
		self.age = inc_age

	def __str__(self):
		return f'{self.name}({self.age})'

	def printName(self):
		print(f'My name is {self.name}')

	def printAge(self):
		print(f'I am {self.age} years old')

	def howLongUntil(self, future_age):
		return future_age - self.age

if __name__ == "__main__":
	myFriendDan = Person('Dan', 40)
	myFriendBrett = Person('Brett', 40)
	print(myFriendDan.name)
	print(myFriendDan.age)
	print(myFriendDan)
	myFriendDan.printName()
	myFriendDan.printAge()
	myFriendDan.age = 41
	myFriendDan.printAge()
	myFriendDan.species = 'Mutant'
	print('Dan is:', myFriendDan.species, 'Brett is:', myFriendBrett.species)
	print(myFriendBrett.howLongUntil(65))
	del myFriendDan
	del myFriendBrett