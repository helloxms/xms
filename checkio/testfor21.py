###
#Manacher line
###

def get_longest_pos(text):
	ss = "#" + "#".join(text) + "#"
	i = 0
	mx = 0
	id = 0
	maxpos = 0
	maxnum = 0
	p = [0 ] * len(ss)
	while i<len(ss):
		if mx > i:
		  p[i] = min(p[ 2*id-i],mx-i)
		else:
		  p[i] = 1
	
		while i-p[i] >=0 and i+p[i] < len(ss) and ss[i-p[i]]==ss[i+p[i]]:
		  p[i] += 1
		 
		if mx < p[i]+i:
		  mx = p[i] + i
		  id = i
		i+=1    
	#print("ss=",ss, "p=",p)
	for i in range(0, len(ss)):
		if maxnum < p[i]:
			maxpos = i
			maxnum = p[i]
	#print( maxpos, maxnum)
	i = 1
	value =ss[maxpos]
	#print("value=",value)
	while i < min(maxpos, len(ss)-maxpos):
		#print(i, ss[maxpos-i], ss[maxpos+i])
		if ss[maxpos-i] == ss[maxpos+i]:
			value = ss[maxpos-i]+value+ss[maxpos+i]
			#print("value=",value)
		else:
			break
		i +=1
	value = value.replace('#','')
	print("result=",value)
	return value

def longest_palindromic(text):
	return get_longest_pos(text)

if __name__ == '__main__':
	longest_palindromic("abc") 
	assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
	assert longest_palindromic("abacada") == "aba", "The First"
	assert longest_palindromic("aaaa") == "aaaa", "The A"