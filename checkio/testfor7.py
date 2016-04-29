def checkio(matrix):
    #replace this for solution
	print("checkio")
	mylist = []
	for i in range(0, 10):
		mylist.append( str( int('0')+i) *4)
	totalstrlist=[]
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix)):
			totalstrlist.append( str( int('0') + matrix[i][j] ))
		totalstrlist.append(',')
	
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix)):
			totalstrlist.append( str( int('0') + matrix[j][i] ) )
		totalstrlist.append(',')

	WN_ES_list=[]
	# y = x + offset
	# offset = -len(matrix)  ~ len(matrix)
	for offset in range(0 , len(matrix)):
		for i in range(0, len(matrix)):
			j = i + offset
			if( i>=0 and j>=0 and j < len(matrix) ):
				totalstrlist.append( str( int('0') + matrix[i][j]) )
		totalstrlist.append(',')

	for offset in range(0 , len(matrix)):
		for i in range(0, len(matrix)):
			j = i - offset
			if( i>=0 and j>=0 and j < len(matrix)):
				totalstrlist.append( str( int('0') + matrix[i][j]) )
		totalstrlist.append(',')
	
	# y = -x + offset
	# offset = 0~ len(matrix)*2
	for offset in range(0, len(matrix)*2 ):
		for i in range(0, len(matrix) ):
			j = i*(-1) + offset
			if( i>=0 and j>=0 and j < len(matrix)):
				totalstrlist.append( str( int('0') + matrix[i][j]) )
		totalstrlist.append(',')
	
	mystring = ''.join(totalstrlist)
	print(mystring)
	print("end of print")	
	for item in mylist:
		if mystring.find( item) >= 0:
			return True
	
	return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
