#this is the space to test new code
from time import sleep
import RPi.GPIO as iop
iop.setmode(iop.BCM)
pins = (2,3,4,17,22,27,10,9,11,5,6,13,19,26,21,20)
for i in pins:
	print (i)

for i in pins:
	iop.setup(i, iop.IN)
	print ("pin " + str(i) + "is setup :)")

try:
	while True:
		if iop.input(2)==0:
			print ("Closed")
		else:
			print ("Open")
		sleep(0.2)
finally:
	iop.cleanup()
