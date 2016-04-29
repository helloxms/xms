mymin = lambda x, y:x > y;
mymax = lambda x, y:x < y;
	
def minmax_single(key, *args):
	print("minmax_single args:",args)
	res = args[0]
	print("minmax_single args[0]=",res)
	for arg in args[1:]:
		if key(res, arg):
			res = arg		
	print("result=",res)
	return res


def minmax_list(key, *args):
	print("minmax_list args=",args)
	print("minmax_list args[0]=",args[0])
	mylist=[]
	
	if isinstance(args[0],type([])):
		for item in args:
			print("item=",item)	
			rr = minmax_single(key, *item)
			mylist.append(rr)
		myitem = minmax_single(key,*mylist)
		for item in args:
			if myitem in item:
				return item
	else:
		return minmax_single(key,*args)
			
				

	
print (minmax_list(mymin, 4, 2, 1, 3, 4, 5, 6, 7)) #will print 1
print (minmax_list(mymax, 4, 2, 1, 3, 4, 5, 6, 7)) #will print 7
print (minmax_list(mymax, [1,0],[2,7]) ) 