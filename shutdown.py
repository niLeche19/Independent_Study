import RPi.GPIO as iop
from time import sleep
from os import system

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
	if iop.input(20) == 0:
		sleep(1)
		if iop.input(20) == 0:
			print("Shutting down :)")
			system('sudo shutdown now')
iop.cleanup
