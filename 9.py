def unique(x):
	y = [] #uniques values
	z = [] #duplicates
	for i in x:
		if i not in y:
			y.append(i)
		else:
			z.append(i)

	return str(list(set(y) - set(z)))


print(unique([1,2,3,1,3]))	