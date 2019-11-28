#this file contains the coded needed to send key reports
import RPi.GPIO as iop
iop.setmode(iop.BCM)
# 12 is setup seperatly for OS toggle switch
iop.setup(12, iop.IN, pull_up_down=iop.PUD_UP)

def writeit(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
	

#write it
# IOP(12) is the OS set switch, posistion 1 is macos and posistion 0 is windows. It switches between ctrl and meta
def writeit(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report)

#send it
def sendit(mod, char):
	print(iop.input(12))
	if mod == 16 and iop.input(12) == 1:
		modOS = 8
	if mod == 8 and iop.input(12) == 0:
		modOS = 16

	if mod == 0:
		writeit(bytes([0, 0, char, 0, 0, 0, 0, 0]))
		writeit(bytes([0, 0, 0, 0, 0, 0, 0, 0]))
	else:
		writeit(bytes([modOS, 0, char, 0, 0, 0, 0, 0]))
		writeit(bytes([0, 0, 0, 0, 0, 0, 0, 0]))

def one():
	sendit(0, 30)
	sendit(32, 30)
	
def two():
	sendit(32, 9)
	
def three():
	sendit(32, 9)
	
def four():
	sendit(32, 9)
	
def five():
	sendit(16, 23)
	
def six():
	sendit(32, 9)
	
def seven():
	sendit(32, 9)
	
def eight():
	sendit(32, 9)
	
def nine():
	sendit(16, 26)
	
def ten():
	sendit(32, 9)
	
def eleven():
	sendit(32, 9)
	
def twelve():
	sendit(32, 9)
	
def thirteen():
	sendit(0, 232)
	
def fourteen():
	sendit(32, 9)
	
def fifteen():
	sendit(32, 9)
	
def sixteen():
	sendit(32, 9)
	
functions = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen]
