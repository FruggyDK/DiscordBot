import random
import time
from prettytable import PrettyTable
import math
import progressbar
from pyfiglet import Figlet

#todo: implement progressbar(using runs)
#code for progress: 
#def example10():
    #widgets = ['Processed: ', Counter(), ' lines (', Timer(), ')']
    #pbar = ProgressBar(widgets=widgets)
    #for i in pbar((i for i in range(150))):
        #time.sleep(0.1)

#lists
diceList = []
results = []
resultsTime = []

#loop varibles
checktotal = 0
count = 0  
output =  PrettyTable()

#user-inputs 
outputState = False

f = Figlet(font='slant')
print(f.renderText('DnD Dice Simulator'))

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

def processTime(start, end):
	return end - start

#essentiel varibles for  mainloop
maxTotal = maxTotal(dice, numberOfDice)


for x in range(runs):
	start = time.time()
	countdown = possibilities(dice, numberOfDice)
	while checktotal != maxTotal:
		for i in range(numberOfDice):
			diceList.append(random.randint(1,dice))
		print("\t| Run {0} of {1} | Roll {2} of {3}".format(x+1, runs, count, countdown), end="\r")
		checktotal = total(diceList)
		count += 1
		countdown -= 1
		if checktotal != maxTotal:
			diceList.clear()
	else:
		end = time.time()
		results.append(count)
		resultsTime.append(processTime(start, end))
		checktotal = 0
		count  =  0
else:
	results.sort()
	resultsTime.sort()
	if outputState == True:
		output.field_names = ["Run#","#Rolls", "#Rolls compaired to statistics","Time(seconds)"]
		output.align["Run#"] = "l"  #aligns the text to the left
		output.align["#Rolls"] = "l"
		output.align["#Rolls compaired to statistics"] = "c"
		for z in range(runs):
			output.add_row([(z+1),(results[z]), results[z] - possibilities(dice, numberOfDice),resultsTime[z]])
		else:
			print(output)
			print("Average number of rolls:",listAverage(results))
			print("Average amount of time per run:",listAverage(resultsTime))
	else:
		output.field_names = ["#", "Min", "Average", "Max"]
		output.add_row(["Rolls(runs={0}):".format(runs), min(results), listAverage(results), max(results)])
		output.add_row(["Time(seconds):", min(resultsTime), listAverage(resultsTime), max(resultsTime)])
		print(output)
