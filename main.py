
"""
#########################################################################
Author: Nick Lee							#
Project: Macro keyboard							#
#########################################################################
"""

from time import sleep
from os import system
import RPi.GPIO as iop
import keys, pinconfig

iop.setmode(iop.BCM)
NULL_CHAR = chr(0)

pins = (2,3,4,17,27,22,10,9,11,20,5,6,13,19,26,21)
tstpins = (2,27,11,13)

keysdown = []
cansend = 1

for i in pins:
	iop.setup(i, iop.IN, pull_up_down=iop.PUD_UP)

iop.setup(18, iop.IN, pull_up_down=iop.PUD_UP) # 18 is setup seperatly for OS toggle switch
#iop.setup(PIN, iop.IN, pull_up_down=iop.PUD_UP) # this is setup seperatly for pin config enter
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
		sleep(0.09)
		#print(iop.input(18), keys.OS)
		if iop.input(PIN) == 0:
			while iop.input(PIN) == 0:
				time.sleep(0.05)
			
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
					if cansend == 1:
						keys.functions[i]()
					keysdown.append(newi)
					
			elif iop.input(newi) == 1: #checks list for released keys
				if lstscn(keysdown, newi) == True:
					keysdown.remove(newi)

finally:
	print ("Goodbye!")
