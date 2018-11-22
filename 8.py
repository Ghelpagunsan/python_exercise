def duplicate(x):
	y = []
	for i in x:
		if i not in y:
			y.append(i)
	y.sort()
	return str(y)
	

print(duplicate([1,3,2,3,2,6,2]))