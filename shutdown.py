import RPi.GPIO as iop
from time import sleep
from os import system
import pinconfig

iop.setmode(iop.BCM)
iop.setup(16, iop.IN, pull_up_down=iop.PUD_UP)
iop.setup(23, iop.IN, pull_up_down=iop.PUD_UP)

cansend = 1

while True:
	if iop.input(23) == 0 and cansend == 1:
		print("This works")
		while iop.input(23) == 0:
			time.sleep(0.02)
			#cansend = 0
		system('sudo python3 /home/pi/Independent_Study/pinconfig.py')
	
	if iop.input(16) == 0:
		sleep(0.3)
		if iop.input(16) == 0:
			print("Shutting down :)")
			system('sudo python3')
			#system('sudo shutdown now')
iop.cleanup
