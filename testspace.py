#this is the space to test new code
import RPi.GPIO as iop
iop.setmode(iop.BCM)
pins = (2,3,4,17,22,27,10,9,11,5,6,13,19,26,21,20)
for i in pins:
	print (i)
for i in pins:
	iop.setup(i, iop.IN)

try:
	while True:
		for i in pins:
			if iop.input(i)==0:
				print ("Closed")
			else:
				print ("Open")
finally:
	iop.cleanup()
