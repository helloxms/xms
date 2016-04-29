
def get_common_num( data ):
	#print("input data=",data)
	lastpos = 8
	
	for i in range(0,8):
		a = [x[i] for x in data]
		if len( set(a) ) != 1:
			lastpos = i
			break;
	
	#print("get_common_num lastpos=",lastpos)
	result = data[0][0:lastpos]
	if( lastpos < 8):
		result = result + '0'*(8-lastpos)
	#print("get_common_num result=",result)
	return result,lastpos
	
def convert_to_bin( data):
	ss = bin(int(data))
	ss = ss[2:]
	if len(ss) < 8:
		a = '0'*(8 - len(ss))
		ss = a+ss
	return ss

def checkio(data):
	#replace this for solution
	mylist=[]
	for item in data:
		ls = item.split('.')
		for i in range(0, len(ls)):
			ls[i] = convert_to_bin(ls[i])
		mylist.append(ls)
	
	#print("mylist=", mylist)
	myresult = []
	subnet = 0
	for i in range(0,4):
		ss,lastpos = get_common_num([ x[i] for x in mylist ])
		#print("ss=",ss)
		myresult.append( str(int(ss,2)) )	
		subnet += lastpos
		if lastpos < 8:
			for j in range(i+1, 4):
				myresult.append('0')
			break;
		
	results = '.'.join(myresult)
	results = results+"/"+str(subnet)
	##print("my results=",results)
	return results

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
	assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
	assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
	
