import RPi.GPIO as iop
from time import sleep
from os import system

iop.setmode(iop.BCM)
iop.setup(16, iop.IN, pull_up_down=iop.PUD_UP)
iop.setup(12, iop.IN, pull_up_down=iop.PUD_UP)

while True:
	if iop.input(16) == 0:
		sleep(0.3)
		if iop.input(16) == 0:
			print("Shutting down :)")
			system('sudo shutdown now')
iop.cleanup
