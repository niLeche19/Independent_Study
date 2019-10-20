#this is the space to test new code
from time import sleep
import RPi.GPIO as iop
iop.setmode(iop.BCM)
pins = (27,2,3,4,17,22,10,9,11,5,6,13,19,26,21,20)

for i in pins:
	iop.setup(i, iop.IN, pull_up_down=iop.PUD_UP)
	print ("pin " + str(i) + "is setup :)")

sleep(3)
tstpins = (2,11,13,27)
keysdown = []

try:
	while True:
		pressed = 0
		keysdown = []
		for i in tstpins:
			if iop.input(i)==0:
				#print ("Key " + str(i) + " pressed")
				pressed = 1
				keysdown.append(i)
		if pressed == 0:
			print ("Open")
		else:
			print (keysdown)

		sleep(0.06)
		
		"""
		if iop.input(27)==0:
			print ("Closed")
			sleep(0.1)
		elif iop.input(2)==0:
			print ("pin2!")
			sleep(0.1)
		elif iop.input(13)==0:
			print ("pin13!")
			sleep(0.1)
		else:
			print ("Open")
			sleep(0.1)
		"""
finally:
	print ("Goodbye!")
