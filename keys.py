#this file contains the coded needed to send key reports

import funcread
import RPi.GPIO as iop
iop.setmode(iop.BCM)

# 12 is setup seperatly for OS toggle switch
iop.setup(12, iop.IN, pull_up_down=iop.PUD_UP)
# 1 in windows and 0 is OSX. It switches between ctrl and meta(win/cmd)
OS = 2

#write it
def writeit(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report)

#executes the list of keystrokes
def keyexc(wlst):
	print(len(wlst))
	for i in range(len(wlst)):
		sendit(wlst[i][0], wlst[i][1])

#send it
def sendit(mod, char):
	modOS = 16
	
	if mod == 16 and OS == 1:
		modOS = 8
	elif mod == 8 and OS == 0:
		modOS = 16
	else: modOS = mod
	if mod == 0:
		writeit(bytes([0, 0, char, 0, 0, 0, 0, 0]))
	else:
		writeit(bytes([modOS, 0, char, 0, 0, 0, 0, 0]))

def funkysendit(key):
	funclist = funcread.readit(key)
	print(funclist)
	keyexc(funclist)

