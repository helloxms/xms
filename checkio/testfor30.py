import itertools
import datetime
table={}
for i in range(10):
	table[i] = str(i)

def d2n(decimal_number, n):
	global table
	result = []
	div, mod = divmod(decimal_number, n)
	result.append(table[mod])
	while div >= n:
		div, mod = divmod(div, n)
		result.append(table[mod])
	result.append(table[div])
	result.reverse()
	return ''.join(result)

str_item_order=[]
for i in range(0, int('555555',base=6)):
	str_item_order.append( d2n(i,6) )
	
dic_item_order={}
for i in range(0, len(str_item_order)):
	stritem = str_item_order[i]
	stritem = '0'*( 6 - len(stritem)) + stritem
	listitem = []
	for k in range(0, len(stritem)):
		pos = int(stritem[k])
		listitem.append( pos )
	dic_item_order[ str_item_order[i] ] = listitem


def checkio(data):
	global str_item_order
	global dict_item_order
	t1 = datetime.datetime.now()
	a = list( itertools.permutations([1,2,3,4,5],5) ) #fix the first triangle
	b = list( itertools.permutations([0,1,2],2) )
	a_filter=[]
	for i in range(0,len(a)):
		aa = list( a[i] )
		#print( aa, a[i], data[0] )
		for j in range(1, len(aa)):
			if  data[aa[j]][0] not in data[j-1] and data[aa[j]][1] not in data[j-1] and data[aa[j]][2] not in data[j-1]:
				continue			
		if  data[aa[4]][0] not in data[0] and data[aa[4]][1] not in data[0] and data[aa[4]][2] not in data[0]:
			continue
		aa.insert(0,0)
		a_filter.append(aa)
	#print(a_filter)
  
	temp = []
	result = 0
	for i in range(0, 6):
		for j in range(0,3):
			temp.append( data[i][j] )
	temp.sort()
	temp.reverse()
	bignum = sum( temp[0:6] )
	len_item_order = int('555555',base=6)
	#t2 = datetime.datetime.now()
	#print( str(t2-t1))
	for i in range(0, len(a_filter)):
		for j in range(0, len_item_order):
			numlist1=[]
			listitem = dic_item_order[ str_item_order[j] ] 

			for l in range(0, len(listitem)):  #l 0-6
				num0 = data[ a_filter[i][l] ][ b[listitem[l] ][0] ]
				num1 = data[ a_filter[i][l] ][ b[listitem[l] ][1] ]
				numlist1.append( num0 )
				numlist1.append( num1 )

			n = numlist1
			if n[1] != n[2] or n[3] != n[4] or n[5] != n[6] or n[7] != n[8] or n[9] != n[10] or n[11] != n[0]:
				continue
			#t4 = datetime.datetime.now()
			#print(str(t4-t2))
			print( n )
			if result < ( sum(temp) -sum(n) ):
				result = sum(temp)-sum(n)
			if result == bignum:
				return result
		print("result=",result)				
	return result

if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"
	
	
