#this file contains the coded needed to send key reports

def writeit(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
	

#write it
def writeit(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report)
#send it
def sendit(mod, char):
	if mod == 0:
		writeit(bytes([0, 0, char, 0, 0, 0, 0, 0]))
		writeit(bytes([0, 0, 0, 0, 0, 0, 0, 0]))
	else:
		writeit(bytes([mod, 0, char, 0, 0, 0, 0, 0]))
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
