import RPi.GPIO as iop
iop.setmode(iop.BCM)

pins = (2,3,4,17,22,27,10,9,11,20,5,6,13,19,26,21)

keysdown = []
cansend = 1

for i in pins:
	iop.setup(i, iop.IN, pull_up_down=iop.PUD_UP)
