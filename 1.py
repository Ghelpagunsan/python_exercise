def lists():
	l = ['Jay', 'Ana', 'Kim', 'Kc']
	a = l[0:2]
	b = l[2:4]
	x = ('A', 'B')
	y= (a)
	d = dict.fromkeys(x, y)
	sorted(d)
	d.update({"B": b})
	return str(d)


print(lists())