def arr_to_dict(key, val):
	a = dict(zip(key,val))
	return str(a)
		
	


print(arr_to_dict(['moe', 'larry', 'curly'], [30,40,50]))