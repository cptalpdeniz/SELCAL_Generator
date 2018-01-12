import random
n = input('How many SELCALs would you like to generate? ')
for i in range(n):
	l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'P', 'Q', 'R', 'S']
	while True:
		selcal1 = random.choice(l)
		if (selcal1 == 'S'):
			continue
		else:
			break
	while True:
		code = random.choice(l) 
		if (selcal1[0] < code):
			selcal1 = selcal1[:] + code
			break
	while True:
		selcal2 = random.choice(l)
		if (selcal1[0] == selcal2 or selcal1[1] == selcal2):
			continue
		if (selcal2 == 'S'):
			continue
		else:
			break
	while True:
		code = random.choice(l)
		if (selcal1[0] == code or selcal1[1] == code):
			continue
		if (selcal2[0] < code):
			selcal2 = selcal2[:] + code
			break
	selcal = selcal1 + '-' + selcal2
	print selcal