# This is the pin configuration file
from time import sleep
import RPi.GPIO as iop
import keys, funcread, funcwrite
combos = {'a': '4', 'b': '5', 'c': '6', 'd': '7', 'e': '8', 'f': '9', 'g': '10', 'h': '11', 'i': '12', 'j': '13', 'k': '14', 'l': '15', 'm': '16', 'n': '17', 'o': '18', 'p': '19', 'q': '20', 'r': '21', 's': '22', 't': '23', 'u': '24', 'v': '25', 'w': '26', 'x': '27', 'y': '28', 'z': '29', '1': '30', '2': '31', '3': '32', '4': '33', '5': '34', '6': '35', '7': '36', '8': '37', '9': '38', '0': '39', 'enter': '40', 'escape': '41', 'back': '42', 'tab': '43', ' ': '44', 'minus': '45', 'equals': '46', 'left_bracket': '47', 'right_bracket': '48', 'backslash': '49', 'pound': '50', 'semicolon': '51', 'quote': '52', 'grave_accent': '53', 'comma': '54', 'period': '55', 'forward_slash': '56', 'caps_lock': '57', 'f1': '58', 'f2': '59', 'f3': '60', 'f4': '61', 'f5': '62', 'f6': '63', 'f7': '64', 'f8': '65', 'f9': '66', 'f10': '67', 'f11': '68', 'f12': '69', 'print_screen': '70', 'scroll_lock': '71', 'pause': '72', 'insert': '73', 'home': '74', 'page_up': '75', 'delete': '76', 'end': '77', 'page_down': '78', 'right_arrow': '79', 'left_arrow': '80', 'down_arrow': '81', 'up_arrow': '82', 'keypad_numlock': '83', 'keypad_forward_slash': '84', 'keypad_asterisk': '85', 'keypad_minus': '86', 'keypad_plus': '87', 'keypad_enter': '88', 'keypad_one': '89', 'keypad_two': '90', 'keypad_three': '91', 'keypad_four': '92', 'keypad_five': '93', 'keypad_six': '94', 'keypad_seven': '95', 'keypad_eight': '96', 'keypad_nine': '97', 'keypad_zero': '98', 'keypad_period': '99', 'keypad_backslash': '100', 'application': '101', 'power': '102', 'keypad_equals': '103', 'f13': '104', 'f14': '105', 'f15': '106', 'f16': '107', 'f17': '108', 'f18': '109', 'f19': '110', 'shift': '02', 'alt': '04', 'control': '01', 'windows': '08', 'command': '08', 'right_control': '16', 'right_shift': '32', 'right_alt': '64', 'right_gui': '128'}

def initiate():
	forwardd = input(" Welcome to the key configurator. \n At any time you can press 'h' for help or 'b' to go back.\n Press enter.\n ")
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
		whichh = 0
		try:
			whichh = int(input(" Which key would you like to edit? (1-16)\n "))
		except:
			print(" Please enter a number (1-16)\n ")
			screenone()
		
		if whichh > 16 or whichh < 1:
			print(" Please enter a number (1-16)\n ")
			screenone()
		
		else: screentwo(whichh - 1)

	elif direc == '':
		screenone()

	else:
		print(" Press 'h' for help.")
		screenone()

def screentwo(key):
	print(" Editting key {}. Press h for help.\n ".format(key + 1))
	nextt = input(" ")
	tmplst = funcread.readit(key)
	print(" Key contents: {}\n".format(tmplst[:len(tmplst) - 1]))
##########
	if nextt == 'h':
		print(" h   : Help.\n q   : Quit.\n b   : Go back.\n c   : Clear the key.\n a   : Add a character to the key.\n m   : Add a modifier to the key.\n d   : Delete a key.\n mc  : Add a modified key. \n s   : Add a string to the key.\n ")
		screentwo(key)
##########
	elif nextt == 'q':
		print(" Seeya later.")
		#main.cansend = 1
##########
	elif nextt == 'b':
		screenone()
##########	
	elif nextt == 'c':
		if input(" Are you sure? (y/n)\n ") == 'y':
			funcwrite.writeit(key, [[0,0]])
			screentwo(key)
		else:
			screentwo(key)
##########
	elif nextt == 'a':
		if len(tmplst) > 1:
			try:
				wheree = int(input(" Where would like to add the new key instance?\n "))
			except:
				print(" Please input a number 1 - {}\n".format(len(tmplst) - 1))
				screentwo(key)
		else:
			wheree = 1
		
		try:	
			ac = input(" What character would you like to add?\n ")
			tmplst.insert(wheree - 1, [0,int(combos[ac])])
			funcwrite.writeit(key, tmplst)
			screentwo(key)
		except:
			print(" Please input an alphanumerical.\n")
			screentwo(key)
##########
	elif nextt == 'm':
		#am = input(" Which modifier would you like to add?\n ")
		if len(tmplst) > 2:
			try:
				wheree = int(input(" Which instance would you like to add the modifier to?\n "))
			except:
				print(" Please input a number 1 - {}\n".format(len(tmplst)))
				screentwo(key)
		else:
			wheree = 1
			
		try:
			am = input(" Which modifier would you like to add?\n ")
			tmplst[wheree - 1][0] += int(combos[am])
			funcwrite.writeit(key, tmplst)
			screentwo(key)
		except:
			print(" Please input a valid modifier, see documentation for list of accepted mods.\n ")
			screentwo(key)
		
##########
	elif nextt == 'd':
		if len(tmplst) > 1:
			try:
				whichh = int(input(" Which instance would you like to delete? (1-{})\n ".format(len(tmplst) - 1)))
				if whichh < 1 or whichh > len(tmplst) - 1:
					print(" Please input a number 1 - {}\n".format(len(tmplst) - 1))
					screentwo(key)
				else:
					del tmplst[whichh - 1]
					funcwrite.writeit(key, tmplst)
					screentwo(key)
			except:
				print(" Lol something is wrong but i couldnt tell you what... \n ")
				screentwo(key)
		else:
			print(" There are no instances to delete in this key.\n ")
			screentwo(key)
##########
	elif nextt == 'mc':
		if len(tmplst) > 1:
			try:
				wheree = int(imput(" Where would like to add the new key instance?\n "))
			except:
				print(" Please input a number 1 - {}\n".format(len(tmplst) ))
				screentwo(key)
		else:
			wheree = 1
		try:
			ac = input(" Which character would you like to add?\n ")
			am = input(" Which modifier would you like to add?\n ")
			tmplst.insert(0,[int(combos[am]), int(combos[ac])])
			funcwrite.writeit(key, tmplst)
			screentwo(key)
		except:
			print(" Please input a valid character/modifier, see documentation for list of valid chars/mods.\n ")
			screentwo(key)
##########
	elif nextt == 's':
		if len(tmplst) > 1:
			wheree = input(" Where wpuld you like to add the string?\n ")
		else:
			wheree = 1
		
		try:
			strr = input(" Please enter your string.\n ")
			for i in strr:
				tmplst.insert(len(tmplst) - 1, [0,combos[i]])
			funcwrite.writeit(key, tmplst)
			screentwo(key)
		except:
			print(" The string can only contain lower case alphanumericals.\n Modifers can be added later.\n ")
			screentwo(key)
			

##########
	elif nextt == '':
		screentwo(key)
##########
	else:
		print(" Press 'h' for help.")
		screentwo(key)
		
		
