import random
import datetime  as  dt
from prettytable import PrettyTable
import math

#lists
diceList = []
results = []
resultsTime = []

#loop varibles
checktotal = 0
count = 0  

#user-inputs 

dice = int(input('''Which dice would you like to roll? (input the number of sides)
> '''))   #sides
numberOfDice = int(input('''How many dice should be rolled?
> ''')) 
runs = int(input('''How many times would you like to test it?
> ''')) 


#functions
def maxTotal(dice, numberOfDice):
	return dice * numberOfDice 

def total(list):
	total = 0
	for item in list:
		total += item
	else:
		return total

def listAverage(list):
	return total(list) /  len(list)

def possibilities(dice, numberOfDice):
	return int(math.pow(dice, numberOfDice))

#def processTime(start, end):
	#return end - start

#def progress(arg1, arg2):
	#return (arg1 / arg2) * 100

#essentiel varibles for  mainloop
maxTotal = maxTotal(dice, numberOfDice)

for x in range(runs):
	countdown = possibilities(dice, numberOfDice)
	#start = dt.datetime.now()
	while checktotal != maxTotal:
		for i in range(numberOfDice):
			diceList.append(random.randint(1,dice))
		print(x+1,"/",runs," | ",count," | ",countdown," | ")	
		checktotal = total(diceList)
		count += 1
		countdown -= 1
		if checktotal != maxTotal:
			diceList.clear()
	else:
		#end =  dt.datetime.now()
		results.append(count)
		#resultsTime.append(processTime(start, end))
		checktotal = 0
		count  =  0
else:
	results.sort()
	#resultsTime.sort()
	#print(resultsTime)
	output =  PrettyTable()
	output.field_names = ["Run#","#Rolls", "#Rolls compaired to statistics"]
	output.align["Run#"] = "l"  #aligns the text to the left
	output.align["#Rolls"] = "l"
	output.align["#Rolls compaired to statistics"] = "c"
	for z in range(runs):
		output.add_row([(z+1),(results[z]), results[z] - possibilities(dice, numberOfDice)])
	else:
		print(output)
		print("Average number of rolls:",listAverage(results))



#make mainloop a function, where  you  can  choose how  it the result should  be printet:
#minimal shows only min, max, and average; full, which  shows all data entries(not recommended if runs > 1000)