# This is the pin configuration file
from time import sleep
import RPi.GPIO as iop
import keys

def 
def initiate():
	forwardd = input(" Welcome to the key configurator. \n At any time you can press 'h' for help or 'b' to go back.\n ")
	#main.cansend = 0
	screenone()
	
def screenone():
	direc = input(" ")
	if direc == 'h':
		print(" h   : Help. \n q   : Quit.\n e   : Edit a key.\n b   : Go back to main screen.")
		screenone()
	
	elif direc == 'q':
		print(" Seeya later.")
		#main.cansend = 1

	elif direc == 'b':
		initiate()
		
	elif direc == 'e':
		whichh = input(" What key would you like to edit?\n ")
		whichh = int(whichh)
		if whichh > 16 or whichh < 1:
			print(" Please enter a number (1-16)\n ")
			screenone()
		else: screentwo(whichh)

	elif direc == '':
		screenone()

	else:
		print(" Press 'h' for help.")
		screenone()
	
def screentwo(key):
	nextt = input(" ")
	if nextt == 'h':
		print(" h   : Help.\n q   : Quit.\n b   : Go back.\n c   : Clear the key.\n a   : Add a character to the key.\n m   : Add a modifier to the key.\n d   : Set key to a string.\n s   : Add string.\n ")
	
	if nextt == 'q':
		print(" Seeya later.")
		#main.cansend = 1
	
	if nextt == 'b':
		screenone()
	
	elif nextt == 'c':
		if input("Are you sure? (y/n)") == 'y':
			del keys.lists[key - 1][:]
			keys.lists[key - 1] += 0, 0
			screentwo(key)
		else:
			screentwo(key)
	elif nextt == 'a':
		print("adding character")
		addchar = input("What character would you like to add?\n ")
		
	elif nextt == 'm':
		print("adding modifier")
	elif nextt == 'd':
		print("adding mod+key")
	elif nextt == 's':
		print("adding string to key")
	
	elif nextt == '':
		screentwo(key)

	else:
		print(" Press 'h' for help.")
		screentwo(key)
		
		
