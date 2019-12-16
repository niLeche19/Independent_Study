
lines = []
lines2 = []
keyss = []
decimals = []
with open('kc.txt', 'r') as r:
    lines = r.readlines()
print(lines)
for i in lines:
    for j in range(len(i)):
        if i[j] == ' ':
            keyss.append('{}'.format(i[:j]))
            decimals.append('{}'.format(int(i[j + 1:], 16)))
            lines2.append(['{}'.format(i[:j]), int(i[j + 1:], 16)])

print(lines2, '\n',keyss, '\n', decimals)
