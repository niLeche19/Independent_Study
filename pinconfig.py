from time import sleep
import RPi.GPIO as iop

screen = 1

def initiate():
	forwardd = input(" Welcome to the key configurator. \n At any time you can press 'h' for help or 'b' to go back.\n")
	screen = 1
	screenone()
	
def screenone():
	direc = input("")
	if direc == 'h':
		print(" h   : Help. \n q   : Quit.\n e   : Edit a key.")
		screenone()
	elif direc == 'q':
		print("Seeya later.")
	elif direc == 'e':
		whichh = input("What key would you like to edit?")
		if whichh > 16 or whichh < 1:
			print("Please enter a number (1-16)")
		else: screentwo(whichh)
	else:
		print("Press 'h' for help.")
		screenone()
	
def screentwo(key):
	return('')
