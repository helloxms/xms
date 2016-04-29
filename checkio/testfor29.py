myitems = [0,1,2,3,4,5]
mydict={}

def initdict(matrix):
	global mydict
	for item in myitems:
		mydict[ str(item) ]= 0


def get_ajacent_area( i, j, matrix):
	area =[]
	if i-1 >= 0:
		area.append( (i-1,j) )
	if j-1 >= 0:
		area.append( (i,j-1) )
	if i+1 <= len(matrix)-1:
		area.append( (i+1, j) )
	if j+1 <= len(matrix) -1:
		area.append( (i, j+1) )
	return area

def find_a_adjacent_item(matrix, curlist , item ):
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix)):
			if (i,j) in curlist:
				continue
			if matrix[i][j] == item:
				area = get_ajacent_area(i,j,matrix)
				#print("cur(i,j)=(%d,%d)"%(i,j))
				#print("cur area:", area)
				for aa in area:
					if aa in curlist:
						curlist.append( (i,j) )
						return True
				
	return False
		
		
def checkio(matrix):
	global mydict
	global myitems
	initdict(matrix)
	for ii in range(0,len(matrix)):
		for jj in range(0,len(matrix)):
			#calc connected array for every cell
			curlist= [(ii,jj) ]
			flag = matrix[ii][jj]		
			for i in range(0, len(matrix)):
				for j in range(0, len(matrix)):
					if matrix[i][j] == flag:
						#print(" matrix[%d][%d]="%(i,j),matrix[i][j]  )
						#print(" curlist=",curlist)
						find_a_adjacent_item( matrix, curlist, flag )
			#print(curlist, len(curlist))
			if mydict[str( flag) ] < len(curlist):
				mydict[str(flag)] = len(curlist)
	
	print(mydict)
	result = [0,0]
	for k,v in mydict.items():
		if result[0] < v:
			result[0] = v
			result[1] = int(k)
	return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([
	    [1, 2, 3, 4, 5],
	    [1, 1, 1, 2, 3],
	    [1, 1, 1, 2, 2],
	    [1, 2, 2, 2, 1],
	    [1, 1, 1, 1, 1]
	]) == [14, 1], "14 of 1"

	assert checkio([
	    [2, 1, 2, 2, 2, 4],
	    [2, 5, 2, 2, 2, 2],
	    [2, 5, 4, 2, 2, 2],
	    [2, 5, 2, 2, 4, 2],
	    [2, 4, 2, 2, 2, 2],
	    [2, 2, 4, 4, 2, 2]
	]) == [19, 2], '19 of 2'
	