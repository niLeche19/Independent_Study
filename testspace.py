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
<<<<<<< HEAD
		for i in (2,27,11,13):
			if iop.input(i)==0:
				print ("Closed")
			else:
				print ("Open")
=======
		if iop.input(2)==1:
			print ("Closed")
>>>>>>> 4b2ba74ee0ae92193c805b823010a744515bb9da
finally:
	iop.cleanup()
