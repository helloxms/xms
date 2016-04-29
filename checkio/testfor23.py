

def myminmax(*args, **kwargs):
	print(kwargs)
	myfunc = kwargs.get("func",None)
	key = kwargs.get("key", None)

	if len(args) == 1:
		args = args[0]
	args = list(args)
	myargs = args
	print("myargs=",myargs)
	if key:
		myargs=[ key(x) for x in args]

	res = myargs[0]
	for arg in myargs[1:]:
		if myfunc(res, arg):
			res = arg			

	for arg in args:
		if key and key(arg) == res:
			print("result arg=",arg)
			return arg
		elif not key:
			print("result res=",res)
			return res

	return None

def min(*args, **kwargs):

	kwargs["func"]=lambda x, y:x > y
	return myminmax(*args, **kwargs )

def max(*args, **kwargs):

	kwargs["func"] =lambda x, y:x < y
	return myminmax(*args, **kwargs)



if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert max(3, 2,key=int) == 3, "Simple case max"
	assert min(3, 2) == 2, "Simple case min"
	assert max([1, 2, 0, 3, 4]) == 4, "From a list"
	assert min("hello") == "e", "From string"
	assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
	assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
	min(abs(i) for i in range(-10, 10))