#this is the space to test new code
"""
#########################################################################
Author: Nick Lee							#
Project: Macro keyboard							#
#########################################################################
"""

from time import sleep
import RPi.GPIO as iop
import pyautoguy as pag

iop.setmode(iop.BCM)
pins = (27,2,3,4,17,22,10,9,11,5,6,13,19,26,21,20)
tstpins = (2,11,13,27)
keysdown = []

for i in pins:
	iop.setup(i, iop.IN, pull_up_down=iop.PUD_UP)
	print ("pin " + str(i) + "is setup :)")

def lstscn (l, n):
	fls = 0
	
	if l != []:
		for i in l:
			if i == n:
				fls = 1
	if fls == 0:
		return (False)
	else:
		return (True)	

try:
	while True:
		pressed = 0
		
		for i in tstpins:
			fals = 1
			if iop.input(i)==0:
				pressed = 1
				if lstscn (keysdown, i) == False:
					print (i)
					keysdown.append(i)
					
			elif iop.input(i)==1:
				if lstscn(keysdown, i) == True:
					keysdown.remove(i)

finally:
	print ("Goodbye!")
