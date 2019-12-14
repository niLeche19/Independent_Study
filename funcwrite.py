
convert = ""

def writeit(line, content):
	with open('kc.txt', 'r') as rr:
		lines = rr.readlines()

	for i in content:
		convert += ("{},{}-\n".format(i[0], i[1]))
	
	del lines[line - 1]
	lines.insert(line - 1, convert)

	with open('kc.txt', 'w') as ww:
		ww.writelines(lines)

		
