#this is the space to test new code
"""
#########################################################################
Author: Nick Lee							#
Project: Macro keyboard							#
#########################################################################
"""

from time import sleep
from os import system
import RPi.GPIO as iop
#import pyautogui as pag

iop.setmode(iop.BCM)
pins = (27,2,3,4,17,22,10,9,11,5,6,13,26,21,20)
tstpins = (2,27,11,13)
keysdown = []

for i in pins:
	iop.setup(i, iop.IN, pull_up_down=iop.PUD_UP)
print ("Pins are set up, starting now :)")

# define each set of strokes for each key hear:
def one():
	print(1)
def five():
	print(1)
def nine():
	print(9)
def thirteen():
	print(13)
functions = (one, five, nine, thriteen)

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
		#pressed = 0
		
		for i in range(len(tstpins)):
			newi = tstpins[i]
			fals = 1
			if iop.input(newi) == 0: #checks list for pressed keys
				#pressed = 1
				if lstscn (keysdown, newi) == False:
					print (newi + "yip dip")
					functions[i]()
					"""
					if newi == 2:
						system('sudo python hidtest.py')
					"""
					keysdown.append(newi)
					
			elif iop.input(newi)==1: #checks list for released keys
				if lstscn(keysdown, newi) == True:
					keysdown.remove(newi)

finally:
	print ("Goodbye!")
