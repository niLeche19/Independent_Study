
"""
#########################################################################
Author: Nick Lee							#
Project: Macro keyboard							#
#########################################################################
"""

from time import sleep
from os import system
import RPi.GPIO as iop
import keys#, pinconfig

iop.setmode(iop.BCM)

pins = (2,3,4,17,27,22,10,9,11,20,5,6,13,19,26,21)

keysdown = []
gamer = 0 # add a gamer mode switch to enable rapid fire presses of switches
keyset = 0
lines = []
with open('kc.txt', 'r') as ree:
	lines = ree.readlines()
	keyset = lines[len(lines)]

for i in pins:
	iop.setup(i, iop.IN, pull_up_down=iop.PUD_UP)

# pull_up_down=iop.PUD_UP
iop.setup(23, iop.IN, pull_up_down=iop.PUD_UP) # 23 is going to change what config set you are on
iop.setup(18, iop.IN, pull_up_down=iop.PUD_UP) # 18 is setup seperatly for OS toggle switch

def lstscn (l, n):
	fls = 0
	if l != []: #check for empty list
		for i in l: #scan list to see if key is already pressed
			if i == n:
				fls = 1
	if fls == 0:
		return (False)
	else:
		return (True)	

try:
	while True:
		sleep(0.01)
		if iop.input(18) == 0: 
			keys.OS = 1
		elif iop.input(18) == 1:
			keys.OS = 0
		
		if iop.input(23) == 0:
			while iop.input(23) == 0:
				sleep(0.01)
			if keyset == 3:
				keyset = 0
			else:
				keyset += 1
				
		print(iop.input(23), keyset, (16 * keyset))
		
		for i in range(len(pins)):
			newi = pins[i]
			fals = 1
			# operating system selector
			if iop.input(newi) == 0: #checks list for pressed keys
				if lstscn (keysdown, newi) == False:
					keys.funkysendit(i + (keyset * 16), gamer)
					keysdown.append(newi)
				elif lstscn (keysdown, newi) == True and gamer == 1:
					keys.funkysendit(i + (keyset * 16), gamer)
					
			elif iop.input(newi) == 1: #checks list for released keys
				if lstscn(keysdown, newi) == True:
					if gamer == 1:
						keys.funkysendit(1001, gamer)
						del keysdown[:]
					else:
						keysdown.remove(newi)

finally:
	del lines[len(lines) - 1]
	lines.append(whichset)
	with open('kc.txt', 'w') as wee:
		wee.writelines(lines)
	print ("Goodbye!")

	
	
