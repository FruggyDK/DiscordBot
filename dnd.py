import random
import time
from prettytable import PrettyTable
import math
import progressbar
from pyfiglet import Figlet
import os

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


#functions
def titel(font,  message, space=bool, newLine=bool, clear=bool):
	if clear == True:
		os.system("clear")
	print (Figlet(font='slant').renderText('DnD Dice Simulator'))
	print ("  <v1.0 - Made by Christian Kaae Larsen>")
	print("\n")
	if space == True:
		print("\t"+message)
	else:
		print("  "+message)
	if newLine == True:
		print("\n")
	
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


#user-inputs 
outputState = False

titel("slant", " ", space=False, newLine=True, clear=False)

#improve(limit  to one  line) #make a list with the  input like  [20,6,10]  and then assign the varibles from the  list
dice = int(input('''Which dice would you like to roll? (input the number of sides)
> '''))   #sides
numberOfDice = int(input('''How many dice should be rolled?
> ''')) 
runs = int(input('''How many times would you like to test it?
> ''')) 

goal =  []
for i in  range(numberOfDice):
	goal.append(dice)

message  =  ("Goal: {0} = {1}").format(str(goal), str(total(goal)))

titel("slant", message,space=False, newLine=True, clear=True)

#essentiel varibles for  mainloop
maxTotal = maxTotal(dice, numberOfDice)


for x in range(runs):
	start = time.time()
	countdown = possibilities(dice, numberOfDice)
	while checktotal != maxTotal:
		for i in range(numberOfDice):
			diceList.append(random.randint(1,dice))
		print("  Run {0} of {1} | Roll {2} of {3}".format(x+1, runs, count, countdown), end="\r")
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
		titel("slant", "results:", space=False, newLine=False, clear=True)
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
		titel("slant", "results:", space=False, newLine=False, clear=True)
		output.field_names = ["#", "Min", "Average", "Max"]
		output.add_row(["Rolls(runs={0}):".format(runs), min(results), listAverage(results), max(results)])
		output.add_row(["Time(seconds):", min(resultsTime), listAverage(resultsTime), max(resultsTime)])
		print(output)