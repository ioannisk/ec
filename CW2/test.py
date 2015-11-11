

dic = {'a':1, 'b':2, 'c':3, 'f':8}
list=[]

for i in dic:
	list.append(i)
list.sort()

for l in list:
	print l, dic[l]	
