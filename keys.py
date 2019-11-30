#this file contains the coded needed to send key reports
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
	for i in range(len(wlst)):
		sendit(wlst[i][0], wlst[i][1])

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
		#writeit(bytes([0, 0, 0, 0, 0, 0, 0, 0]))
	else:
		writeit(bytes([modOS, 0, char, 0, 0, 0, 0, 0]))
		#writeit(bytes([0, 0, 0, 0, 0, 0, 0, 0]))

funcone = [[4,0],[8,0],[0,21],[0,0]]
def one():
	writeit(bytes([4,8,21,0,0,0,0,0]))
	#sendit(4,0)
	#sendit(8,0)
	#sendit(0,21)
	#sendit(0,0)
	#keyexc(funcone)

functwo = [[0,0]]
def two():
	sendit(32, 9)

functhree = [[0,0]]
def three():
	sendit(32, 9)
	       
funcfour = [[0,0]]
def four():
	sendit(32, 9)

funcfive = [[0,0]]
def five():
	sendit(16, 23)
	
funcsix = [[0,0]]
def six():
	sendit(32, 9)

funcseven = [[0,0]]
def seven():
	sendit(32, 9)

funceight = [[0,0]]
def eight():
	sendit(32, 9)

funcnine = [[0,0]]
def nine():
	sendit(16, 26)

functen = [[0,0]]
def ten():
	sendit(32, 9)

funceleven = [[0,0]]
def eleven():
	sendit(32, 9)

functwelve = [[0,0]]
def twelve():
	sendit(32, 9)

functhirteen = [[0,0]]
def thirteen():
	sendit(0, 232)

funcfourteen = [[0,0]]
def fourteen():
	sendit(32, 9)

funcfifteen = [[0,0]]
def fifteen():
	sendit(32, 9)

funcsixteen = [[0,0]]
def sixteen():
	sendit(32, 9)

lists = [funcone, functwo, functhree, funcfour, funcfive, funcsix, funcseven, funceight, funcnine, functen, funceleven, functwelve, functhirteen, funcfourteen, funcfifteen, funcsixteen]
functions = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen]
