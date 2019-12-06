
def readit(line):
	with open('kc.txt', 'r') as f:
		lst1 = []
		lst2 = []
		rept = f.readlines()
		f.seek(0)
		ii = 0
		# determine how many functions are contained in the line and add them to 
		for j in rept[line]:
			if j == '-':
				lst2.append([])
		# turns line into list in the format 0,0-0,0-
		for h in rept[line]:
			if h != '-' and h != ',':
				lst1 += str(h)
			elif h == ',':
				lst2[ii].append(int(''.join(lst1)))
				del lst1[:]
			elif h == '-':
				lst2[ii].append(int(''.join(lst1)))
				del lst1[:]
				ii += 1
	return(lst2)
