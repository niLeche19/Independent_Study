
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

pins = (2,3,4,17,22,27,10,9,11,20,5,6,13,19,26,21)

keysdown = []
cansend = 1

for i in pins:
	iop.setup(i, iop.IN, pull_up_down=iop.PUD_UP)
#iop.setup(23, iop.IN, pull_up_down=iop.PUD_UP) # 23 is going to intiate the pin config script
iop.setup(18, iop.IN, pull_up_down=iop.PUD_UP) # 18 is setup seperatly for OS toggle switch
#iop.setup(PIN, iop.IN, pull_up_down=iop.PUD_UP) # this is setup seperatly for pin config enter
#print ("Pins are set up, starting now :)")

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
		sleep(0.09)
		"""
		if iop.input(23) == 0:
			while iop.input(23) == 0:
				time.sleep(0.02)
			pinconfig.initiate()
		"""
		if iop.input(18) == 0: 
			keys.OS = 1
		elif iop.input(18) == 1:
			keys.OS = 0
		
		for i in range(len(pins)):
			newi = pins[i]
			fals = 1
			# operating system selector
			if iop.input(newi) == 0: #checks list for pressed keys
				if lstscn (keysdown, newi) == False:
					if cansend == 1: # this is preventitave for if the config is open
						keys.funkysendit(i)
					keysdown.append(newi)
					
			elif iop.input(newi) == 1: #checks list for released keys
				if lstscn(keysdown, newi) == True:
					keysdown.remove(newi)

finally:
	print ("Goodbye!")

	
	
