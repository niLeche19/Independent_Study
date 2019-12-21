

def writeit(line, content):	
	convert = ""
	with open('kc.txt', 'r') as rr:
		lines = rr.readlines()

	for i in content:
		convert += ("{},{}-".format(i[0], i[1]))
	
	del lines[line]
	lines.insert(line, (convert + "\n"))

	with open('kc.txt', 'w') as ww:
		ww.writelines(lines)

		
