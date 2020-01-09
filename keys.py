#this file contains the coded needed to send key reports

import funcread
OS = 2

#write it
def writeit(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report)

#executes the list of keystrokes
def keyexc(wlst, gg):
	for i in range(len(wlst)):
		if wlst[i] == [0,0] and gg == 1:
			pass
		elif wlst[i] == [0,0] and gg != 1:
			sendit(wlst[i][0], wlst[i][1])
		else:
			sendit(wlst[i][0], wlst[i][1])

#send it
def sendit(mod, char):
	modOS = 1
	"""
	if mod == 1 and OS == 1:
		modOS = 8
	elif mod == 8 and OS == 0:
		modOS = 1
	else: modOS = mod
	"""
	if mod == 0:
		writeit(bytes([0, 0, char, 0, 0, 0, 0, 0]))
	else:
		writeit(bytes([mod, 0, char, 0, 0, 0, 0, 0]))

def funkysendit(key, g):
	
	if key == 1001:
		keyexc([[0,0]], 3)
	else:
		funclist = funcread.readit(key)
		keyexc(funclist, g)

