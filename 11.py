mylist = [{1:'one', 'index':0},{2:'two', 'index':1},{3:'three', 'index':2}]
def findObject(mylist, n):
	b = n['index']
	c = dict()
	for x in mylist:
		if b == x['index']:
			c = x

	print(c)

findObject(mylist, {'index':2})
