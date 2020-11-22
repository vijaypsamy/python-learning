from ast import literal_eval

#Sample user input:

#{'Alice': {'apples': 5, 'pretzels': 12}, 'Bob': {'ham sandwiches': 3, 'apples': 2}, 'Carol': {'cups': 3, 'apple pies': 1}}

def count(allGuests):
	d = {}
	for i in allGuests.values():
		for v in i.keys():
			d.setdefault(v,0)
			d[v] = d[v] + i[v]
	return d
	
print("Enter dictionary")
allGuests = literal_eval(input())
s = count(allGuests)

print(s)
