def non_integer(a):
	b = []
	for x in a:
		if type(x) != type(int()):
			a.remove(x)
		else:
			b.append(x)

	return str(b)


print(non_integer([2,'a', '2', {1: 'one'}]))

