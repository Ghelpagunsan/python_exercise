def check_differences(a, b):
	x = set(a)
	y = set(b)
	z = x - y
	return str(list(z))

print(check_differences([1,2,3,4,5], [5,2,10]))