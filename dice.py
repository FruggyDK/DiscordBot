import random

def average(asum, entries):
	return asum/entries

def dice(dice, numberOfDice):
	slag = []
	if numberOfDice == 1:
		return random.randint(1,dice)
	else:
		for i in range(numberOfDice):
			slag.append(random.randint(1,dice))
		else:
			return '''{0} = {1}
average = {2}'''.format(slag, sum(slag), average(sum(slag), numberOfDice))
