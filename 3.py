def odd(a):
	b = []
	for i in a:
		if i%2!=0:
			b.append(i)

	return str(b)



print(odd([1, 2, 3, 4, 5, 6, 7]))


