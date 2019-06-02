import random

def total(arg1):
	total =  0 
	for item in arg1:
		total += item
	else:
		return total 

def dice(dice, numberOfDice):
	slag = []
	if numberOfDice == 1:
		return random.randint(1,dice)
	else:
		for i in range(numberOfDice):
			slag.append(random.randint(1,dice))
		else:
			return "{0} = {1}".format(slag, total(slag))
