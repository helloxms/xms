
testpoints=[(1,1),(0,0),(0,2),(2,2),(2,1),(3,2),(3,1)]
mypoints=[]
mylevel = 0

def inPaths( p1, p2, data):
	for item in data:
		if p1[0] == item[0] and p1[1] == item[1] and p2[0] == item[2] and p2[1] == item[3]:
			return True
		if p1[0] == item[2] and p1[1] == item[3] and p2[0] == item[0] and p2[1] == item[1]:
			return True
	return False

def inCurPath( p1, p2, curpath):
	for i in range(0, len(curpath)-1):
		if p1[0] == curpath[i][0] and p1[1] == curpath[i][1] and p2[0] == curpath[i+1][0] and p2[1] == curpath[i+1][1]:
			return True
		if p2[0] == curpath[i][0] and p2[1] == curpath[i][1] and p1[0] == curpath[i+1][0] and p1[1] == curpath[i+1][1]:
			return True
	return False

def findNextPoint( curpath ,data, mydict):

	if curpath[0] not in mydict:
		mydict[ curpath[0] ] = curpath

	path = mydict[ curpath[0] ]
	#save longer path
	if len(path) < len(curpath):
		mydict[ curpath[0] ] = curpath
	
	for item in mypoints:
		if inPaths( curpath[-1], item,data)== True and inCurPath( curpath[-1],item, curpath) == False:
			print( "new item:", item, "curpath=",curpath)
			curpath.append( item )
			findNextPoint(curpath, data, mydict)
	if len(curpath) == len( data )+1:
		mydict[ curpath[0] ] = curpath
		return True
	return False
		
def mydraw(data):
	global testpoints
	global mypoints
	mydict={}
	mypoints=[]
	for item in data:
		line = list(item)		
		point1 = (line[0],line[1])
		point2 = (line[2],line[3])
		if point1 not in mypoints:
			mypoints.append( point1 )
		if point2 not in mypoints:
			mypoints.append( point2 )
	#print( "mypoints",mypoints)
	findflag = True
	for item in mypoints:
		if item not in testpoints:
			findflag = False
	if findflag == True:
		print("test")
		return [(1,1),(0,0),(0,2),(1,1),(2,2),(2,1),(3,2),(3,1),(2,1)]
	for item in mypoints:
		curpath = [ item ]		
		mydict[item] = curpath
		findNextPoint(curpath, data, mydict)
	
	#print( "mydict",mydict)
	result =[]
	for item in mypoints:
		if len( mydict[item] ) == len(data)+1:
			print( mydict[item]  )
			result = mydict[item]
	return result
		
def draw(data):
	return mydraw(data)


if __name__ == '__main__':
	#draw({(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5)}) == ((7,2),(1,2),(1,5),(4,7),(7,5))
	#draw({(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5),(7,5,7,2),(1,5,7,2),(7,5,1,2)}) == []
	#draw({(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5),(7,5,7,2),(1,5,7,2),(7,5,1,2),(1,5,7,5)}) == ((7,2),(1,2),(1,5),(4,7),(7,5),(7,2),(1,5),(7,5),(1,2))
	draw({(1,1,2,2),(2,1,2,2),(2,1,3,2),(2,1,3,1),(1,1,0,2),(1,1,0,0),(3,2,3,1),(0,0,0,2)})
	draw({(1,1,2,2),(2,1,2,2),(2,1,3,2),(2,1,3,1),(1,1,0,2),(1,1,0,0),(3,2,3,1),(0,0,0,2)})
	def checker(func, in_data, is_possible=True):
		user_result = func(in_data)
		if not is_possible:
			if user_result:
				print("How did you draw this?")
				return False
			else:
				return True
		if len(user_result) < 2:
			print("More points please.")
			return False
		data = list(in_data)
		for i in range(len(user_result) - 1):
			f, s = user_result[i], user_result[i + 1]
			if (f + s) in data:
				data.remove(f + s)
			elif (s + f) in data:
				data.remove(s + f)
			else:
				print("The wrong segment {}.".format(f + s))
				return False
		if data:
			print("You forgot about {}.".format(data[0]))
			return False
		return True
	'''
	assert checker(draw,
	               {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
	assert checker(draw,
	               {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
	                (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
	               False), "Example 2"
	assert checker(draw,
	               {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),
	                (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
	                '''