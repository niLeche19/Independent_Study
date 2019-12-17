# This is the pin configuration file
from time import sleep
import RPi.GPIO as iop
import keys, funcread, funcwrite
combos = {'a': '4', 'b': '5', 'c': '6', 'd': '7', 'e': '8', 'f': '9', 'g': '10', 'h': '11', 'i': '12', 'j': '13', 'k': '14', 'l': '15', 'm': '16', 'n': '17', 'o': '18', 'p': '19', 'q': '20', 'r': '21', 's': '22', 't': '23', 'u': '24', 'v': '25', 'w': '26', 'x': '27', 'y': '28', 'z': '29', 'one': '30', 'two': '31', 'three': '32', 'four': '33', 'five': '34', 'six': '35', 'seven': '36', 'eight': '37', 'nine': '38', 'zero': '39', 'enter': '40', 'escape': '41', 'backspace': '42', 'tab': '43', 'spacebar': '44', 'minus': '45', 'equals': '46', 'left_bracket': '47', 'right_bracket': '48', 'backslash': '49', 'pound': '50', 'semicolon': '51', 'quote': '52', 'grave_accent': '53', 'comma': '54', 'period': '55', 'forward_slash': '56', 'caps_lock': '57', 'f1': '58', 'f2': '59', 'f3': '60', 'f4': '61', 'f5': '62', 'f6': '63', 'f7': '64', 'f8': '65', 'f9': '66', 'f10': '67', 'f11': '68', 'f12': '69', 'print_screen': '70', 'scroll_lock': '71', 'pause': '72', 'insert': '73', 'home': '74', 'page_up': '75', 'delete': '76', 'end': '77', 'page_down': '78', 'right_arrow': '79', 'left_arrow': '80', 'down_arrow': '81', 'up_arrow': '82', 'keypad_numlock': '83', 'keypad_forward_slash': '84', 'keypad_asterisk': '85', 'keypad_minus': '86', 'keypad_plus': '87', 'keypad_enter': '88', 'keypad_one': '89', 'keypad_two': '90', 'keypad_three': '91', 'keypad_four': '92', 'keypad_five': '93', 'keypad_six': '94', 'keypad_seven': '95', 'keypad_eight': '96', 'keypad_nine': '97', 'keypad_zero': '98', 'keypad_period': '99', 'keypad_backslash': '100', 'application': '101', 'power': '102', 'keypad_equals': '103', 'f13': '104', 'f14': '105', 'f15': '106', 'f16': '107', 'f17': '108', 'f18': '109', 'f19': '110', 'shift': '225', 'alt': '226', 'control': '228', 'windows': '227', 'command': '227', 'right_control': '228', 'right_shift': '229', 'right_alt': '230', 'right_gui': '231'}
lines = []
#with open('kc.txt', 'r') as lip:
#	lines = lip.readlines()

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
		whichh = 0
		try:
			whichh = int(input(" Which key would you like to edit?\n "))
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
	nextt = input(" ")
	tmplst = funcread.readit(key)
	if nextt == 'h':
		print(" h   : Help.\n q   : Quit.\n b   : Go back.\n c   : Clear the key.\n a   : Add a character to the key.\n m   : Add a modifier to the key.\n d   : Set key to a string.\n s   : Add string.\n ")
	
	if nextt == 'q':
		print(" Seeya later.")
		#main.cansend = 1
	
	if nextt == 'b':
		screenone()
	
	elif nextt == 'c':
		if input(" Are you sure? (y/n)\n ") == 'y':
			#tmplst = funcread.readit(key)
			funcwrite.writeit(key, [[0,0]])
			print(tmplst, key)
			#del lines[key - 1]
			#lines.insert((key - 1), '0,0-\n')
		else:
			screentwo(key)

	elif nextt == 'a':
		ac = input(" What character would you like to add?\n ")
		#tmplst = funcread.readit(key)
		try:
			print(combos[ac])
		except:
			print("Please input an alphanumerical")
			screentwo(key)
		"""templst.insert(len(templst) - 1, [0,ord(ac)])""" # this needs to convert a char ('a') into the proper hex HID code
		#funcwrite(key, tmplist)
		
	elif nextt == 'm':
		am = input(" Which modifier would you like to add?\n ")
		tmplst = funcread.readit(key)
		if len(tmplst) > 2:
			amm = input(" Which key would you like the modifier to add too?\n ")
			try:
				print(int('a'))
				#tmplst[i-1][0] += #modifier number
			except:
				screentwo(key)
		else:
			
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
		
		
