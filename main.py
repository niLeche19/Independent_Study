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
import keys

iop.setmode(iop.BCM)
NULL_CHAR = chr(0)

pins = (2,3,4,17,27,22,10,9,11,20,5,6,13,19,26,21)
tstpins = (2,27,11,13)

keysdown = []

for i in pins:
	iop.setup(i, iop.IN, pull_up_down=iop.PUD_UP)

iop.setup(12, iop.IN, pull_up_down=iop.PUD_UP) # 12 is setup seperatly for OS toggle switch

print ("Pins are set up, starting now :)")

"""
def writeit(report):
    with open('/dev/hidg0', 'wb+') as fd:
        fd.write(report.encode())
	
def sendit(mod, charr):
	if mod == 0:
		writeit(chr(0)*2 + chr(charr) + chr(0)*5)
		writeit(chr(0)*8)
	else:
		writeit(chr(mod) + chr(0) + chr(charr) + chr(0)*5)
		writeit(chr(0)*8)
"""	

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
		print(iop.input(12)
		if iop.input(12) == 0: 
			keys.OS = 0
		elif iop.input(12) == 1:
			keys.OS = 1
		for i in range(len(pins)):
			newi = pins[i]
			fals = 1
			# operating system selector
			
			
			if iop.input(newi) == 0: #checks list for pressed keys
				if lstscn (keysdown, newi) == False:
					keys.functions[i]()
					keysdown.append(newi)
					
			elif iop.input(newi)==1: #checks list for released keys
				if lstscn(keysdown, newi) == True:
					keysdown.remove(newi)

finally:
	print ("Goodbye!")
