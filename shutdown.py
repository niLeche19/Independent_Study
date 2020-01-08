import RPi.GPIO as iop
from time import sleep
from os import system

iop.setmode(iop.BCM)
iop.setup(15, iop.IN, pull_up_down=iop.PUD_UP)

while True:
	sleep(0.01)
	if iop.input(15) == 0:
		sleep(0.3)
		if iop.input(15) == 0:
			system('sudo shutdown now')
iop.cleanup
