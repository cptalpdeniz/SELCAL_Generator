import random
n = input('How many SELCALs would you like to generate? ')
for i in range(n):
	l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'P', 'Q', 'R', 'S']
	while True:
		selcal1i = random.choice(range(len(l)))
		selcal1 = l[selcal1i]
		if (selcal1 != 'S'):															#check if first letter of the code is "S"
			break
	code = random.choice(l[selcal1i:])
	selcal1 = selcal1[:] + code
	while True:
		selcal2i = random.choice(range(len(l)))
		selcal2 = l[selcal2i]
		if (selcal1[0] != selcal2 or selcal1[1] != selcal2 or selcal2 != 'S'):			#another check to make sure code is within the rules
			break
	while True:
		code = random.choice(l[selcal2i:])
		if (selcal1[0] == code or selcal1[1] == code):
			continue
		if (selcal2[0] < code):
			selcal2 = selcal2[:] + code
			break
	selcal = selcal1 + '-' + selcal2
	print selcal
