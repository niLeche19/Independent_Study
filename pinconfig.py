from time import sleep
import RPi.GPIO as iop

screen = 1 

def initiate():
	forwardd = input(" Welcome to the key configurator. \n At any time you can press 'h' for help or 'b' to go back.")
        screen = 1
	screenone()
	
def screenone():
	direc = input("")
	if direc == 'h':
		print("h   : Help. \nq   : Quit.\ne   : Edit a key.")
		screenone()
	if direc == 'q':
		print("Seeya later.")
	if direc == 'e':
		whichh = input("What key would you like to edit?")
		if whichh > 16 or whichh < 1:
			print("Please enter a number (1-16)")
		else: screentwo(whichh)
	
def screentwo(key):
	return('')
