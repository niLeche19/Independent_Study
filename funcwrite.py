

def writeit(line, content):	
	convert = ""
	with open('kc.txt', 'r') as rr:
		lines = rr.readlines()

	for i in content:
		convert += ("{},{}-\n".format(i[0], i[1]))
	
	del lines[line]
	lines.insert(line, convert)

	with open('kc.txt', 'w') as ww:
		ww.writelines(lines)

		
