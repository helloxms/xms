import math

def isPrime(n):
	if n<= 1:
		return False
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True
    
smallnums=[]

def getsmallnum(number):
	smallbag = [2,3,5,7]
	bFind = False
	global smallnums
	for item in smallbag:
		if number % item == 0:
			bFind = True
			smallnums.append(item)
			curnum = number/item
			return getsmallnum(curnum)

	if(number>10):
		smallnums.append(number)
	return smallnums

def combinvalue(data):
	data.reverse()
	print(data)
	for i in range(0, len(data)):
		if( data[i] == 3 and data[i] >0 and i+1 < len(data) and data[i+1]>0 ):
			data[i]= data[i]*data[i+1]
			data[i+1]=0
	data = [ i for i in data if i!=0]
	for i in range(0, len(data)):
		if( data[i] ==2 and i+1 < len(data) and data[i+1]==2 and i+2 < len(data) and data[i+2]==2):
			data[i]= data[i]*data[i+1]*data[i+2]
			data[i+1]=0
			data[i+2]=0
	data = [ i for i in data if i!=0]    
	for i in range(0, len(data)):
		if( data[i] == 2 and i+1 < len(data) and data[i+1]==2):
			data[i]= data[i]*data[i+1]
			data[i+1] =0
	data = [i for i in data if i!= 0]
	ss=""
	data.sort()
	for item in data:
		ss += str(item)
	print("ss=",ss)
	return int(ss)

		

def checkio(number):
	#replace this for solution
	if isPrime(number):
		return 0
	global smallnums
	smallnums=[]
	data = getsmallnum(number)
	if( len(data)==0 ):
		return 0
	for item in data:
		if item > 10:
			return 0

	return combinvalue(data)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(20) == 45, "1st example"
	assert checkio(21) == 37, "2nd example"
	assert checkio(17) == 0, "3rd example"
	assert checkio(33) == 0, "4th example"
	assert checkio(3125) == 55555, "5th example"
	assert checkio(9973) == 0, "6th example"