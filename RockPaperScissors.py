""" 
Rock Paper Scissors
---------------------------------------
"""

import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')


playerChoice = []
while (1 < 2):
	print ("\n")
	print ("Welcome to the game: Rock, Paper, Scissors")
	playerChoice = input("Select a weapon [R]ock, [P]aper, or [S]cissor: ")
	if not re.match("[SsRrPp]", playerChoice):
		print ("Wrong choice. Please choose a letter:")
		print ("[R]ock, [P]aper or [s]cissors")
		continue
	print ("You have chosen:" + playerChoice)
	choices = ['R', 'P', 'S']
	machineChoice = random.choice(choices)
	print ("I chose:" + machineChoice)
	if machineChoice == str.upper(playerChoice):
		print ("That is a Tie ;)  Let us break the tie")
		continue
	elif machineChoice == 'R' and playerChoice.upper() == 'S':
		print ("rock beats scissors, you lost ;) ")
		continue
	elif machineChoice == 'S' and playerChoice.upper() == 'P':
		print ("Scissors beats Paper, you lost ;) ")
		continue
	elif machineChoice == 'P' and playerChoice.upper() == 'R':
		print ("Paper beats rock, You lost ;) ")
		continue
	else:
		print ("Congratulations. You Win")
	

