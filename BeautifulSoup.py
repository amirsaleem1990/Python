x = []
for i in s.select('a'):
	try:
		l = i['href']
		if l.startswith("/item/samsung"):
			x.append(i)
	except:
		pass
x = [i['href'] for i in x]


# above is equelent to below
pattern = "^/item/samsung"
x2= s.find_all('a', href=re.compile(pattern))
x2 = [i['href'] for i in x2]



