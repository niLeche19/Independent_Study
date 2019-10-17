#this is the space to test new code

strone = input("what would you like me to break down?")
word = ""
for i  in strone:
	if i != " ":
		word.append(i)
	else:
		print(word)
		word = ""
