import RPi.GPIO as iop
from time import sleep
from os import system

iop.setmode(iop.BCM)
iop.setup(20, iop.IN, pull_up_down=iop.PUD_UP)
while True:
	if iop.input(20) == 0:
		sleep(0.3)
		if iop.input(20) == 0:
			print("Shutting down :)")
			system('sudo shutdown now')
iop.cleanup
