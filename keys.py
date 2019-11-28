#this file contains the coded needed to send key reports
import RPi.GPIO as iop
iop.setmode(iop.BCM)

# 12 is setup seperatly for OS toggle switch
iop.setup(12, iop.IN, pull_up_down=iop.PUD_UP)
OS = 2 # 1 in windows and 0 is OSX. It switches between ctrl and meta(win/cmd)

#write it
def writeit(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report)

def keyexc(wlst):
	for i in range(len(wlst)):
		sendit(wlst[i][0], wlst[i][1])

funcone = [[0, 30], [32, 30]]


#send it
def sendit(mod, char):
	modOS = 16
	print(OS)
	if mod == 16 and OS == 1:
		modOS = 8
	elif mod == 8 and 0:
		modOS = 16
	else: modOS = mod

	if mod == 0:
		writeit(bytes([0, 0, char, 0, 0, 0, 0, 0]))
		writeit(bytes([0, 0, 0, 0, 0, 0, 0, 0]))
	else:
		writeit(bytes([modOS, 0, char, 0, 0, 0, 0, 0]))
		writeit(bytes([0, 0, 0, 0, 0, 0, 0, 0]))

def one():
	keyexc(funcone)
	
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
	
functions = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen]
