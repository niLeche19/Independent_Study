#this is the space to test new code
from time import sleep
import RPi.GPIO as iop
iop.setmode(iop.BCM)
pins = (27,2,3,4,17,22,10,9,11,5,6,13,19,26,21,20)

for i in pins:
	iop.setup(i, iop.IN, pull_up_down=iop.PUD_UP)
	print ("pin " + str(i) + "is setup :)")

tstpins = (2,11,13,27)
keysdown = []


def lstscn (l, n):
	fls = 0
	
	if l != []:
		for i in l:
			if i == n:
				return (True)
				fls = 1
	if fls == 0:
		return (False)
		

try:
	while True:
		pressed = 0
		keysdown = []
		for i in tstpins:
			fals = 0
			if iop.input(i)==0:
				pressed = 1
				if keysdown != []:
					for h in keysdown:
						if i == h:
							fals = 1
				if fals == 0:
					print (i)
				keysdown.append(i)
				print(lstscn(keysdown, i), keysdown, i)

		if pressed == 0:
			print ("All open")
		#else:
		#	print (keysdown)

		sleep(0.2)
		
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
