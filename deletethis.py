from time import sleep
import RPi.GPIO as iop
iop.setmode(iop.BCM)
iop.setup(2, iop.IN, pull_up_down=iop.PUD_UP)

try:
	while True:
		print (iop.input(2))
		if iop.input(2)==0:
			vart = ("What should i print?")
			print(vart)
		sleep(0.2)
finally:
	iop.cleanup()
