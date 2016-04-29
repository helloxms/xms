def check_pangram(text):
    
	text = text.lower()
	mylist= list(set(text))
	mylist.sort()
	myalpha=[]
	for item in mylist:
		if item.isalpha():
			myalpha.append( item)
	
	#print("myalpha=",myalpha)
	result = True
	for i in range(ord('a'), ord('z')+1):
		if chr(i) in myalpha :
			#print("True,chr i=%s in myalpha"%chr(i))
			pass
		else:
			result= False
			#print("False, chr i=%s not in myalpha"%chr(i) )
			break

	return result

if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
	assert not check_pangram("ABCDEF"), "ABC"
	assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"