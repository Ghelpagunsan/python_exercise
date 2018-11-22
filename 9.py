def unique():
	x = [1,2,3,1,3]
	y = [] #uniques values
	z = [] #duplicates
	for i in x:
		if i not in y:
			y.append(i)
		else:
			z.append(i)

	print(list(set(y) - set(z)))


unique()	