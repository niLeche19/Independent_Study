#this is the space to test new code
import RPi.GPIO as iop
iop.setmode(iop.BCM)
pins = (2,3,4,17,22,27,10,9,11,5,6,13,19,26,21,20)
for i in pins:
	print (i)

for i in pins:
	iop.setup(i, iop.IN)
	print ("pin " + i + "is setup :)")

try:
	while True:
		if iop.input(2)==1:
			print ("Closed")
finally:
	iop.cleanup()
