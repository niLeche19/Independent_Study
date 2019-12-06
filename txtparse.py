with open('kc.txt', 'r') as f:
    lst1 = []
    lst2 = []
    lst3 = []
    rept = f.readlines()
    f.seek(0)
    for i in range(1):
        ii = 0
        for j in rept[i]:
            if j == '-':
                lst3.append([])
        for h in rept[i]:
            	if h != '-' and h != ',':
                	lst1.append(i)
            	if h == ',':
			lst3[ii] += lst1
			del lst1[:]
		if h == '-':
			ii += 1
			"""
    print(lst3)
    f.seek(0)
    for i in range(1):
        for j in str(rept[i]):
            print(j)
            if j != '-' and j != ',':
                lst1.append(j)
                print(lst1, lst2)
            if j == ',':
                lst2.append(''.join(lst1))
                print(lst2, lst1)
                del lst1[:]
                
            if j == '-':
                lst2.append(''.join(lst1))
                lst3 += lst2
                print(lst3, lst2)
                print("--- im retarded", lst2, lst1)
                del lst1[:], lst2[:]
                
                
            
            if j == '-':
                lst3.insert(0, lst2)
                del lst2[:], lst1[:]
            elif j == ',':
                lst2.append(lst1)
                del lst1[:]
            else:
                lst1.append(int(j))
            """
    
print(lst1)
print(lst2)
print(lst3)


