def duplicate():
	x = [1,3,2,3,2,6,2]
	y = []
	for i in x:
		if i not in y:
			y.append(i)
	y.sort()
	print(y)
	

duplicate()