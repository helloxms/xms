import math
#min radix = 2 
#max radix = 35
def checkio(strdata):
	strdata = strdata.lower()
	alpha = [ chr(x) for x in range( ord('a'), ord('z')+1) ]
	
	for i in range(2, 36):
		radix = i
		bPassCheck1 = True
		for j in range(0, len(strdata)):
			if strdata[j].isdigit() and int( strdata[j] ) < radix:
				continue
			elif strdata[j].isalpha() and (10 + ord(strdata[j]) -ord('a') )< radix:
				continue
			else:
				bPassCheck1 = False
				continue
		if bPassCheck1 == True:
			mysum = 0
			for k in range(0,len(strdata)):
				if strdata[k].isdigit():
					mysum = mysum + math.pow( radix,  len(strdata)-k-1)*int(strdata[k])
				elif strdata[k].isalpha():
					mysum = mysum + math.pow( radix,  len(strdata)-k-1)*int(ord(strdata[k])-ord('a')+10)
			if mysum%(radix-1) == 0:
				print(radix)
				return radix
	print(0)
	return 0
	
	
if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(u"18") == 10, "Simple decimal"
	assert checkio(u"1010101011") == 2, "Any number is divisible by 1"
	assert checkio(u"222") == 3, "3rd test"
	assert checkio(u"A23B") == 14, "It's not a hex"
	assert checkio(u"IDDQD") == 0, "k is not exist"
	print('Local tests done')
			
		
			
		
