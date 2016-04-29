
#需要学习一下re 相关的方法 match 等

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
import string
def IsStripedWords(data):
	if(len(data) <= 1):
		return False
	data = data.upper()      
	print(data)  
	result = True
	for i in range(0, len(data)):
		if data[i] in VOWELS and i%2 == 0:
			continue
		elif data[i] in CONSONANTS and i%2 == 1:
			continue
		else:
			result = False
			break;
			
	if result == False:
		result = True
		for j in range(0,len(data)):
			if data[j] in CONSONANTS and j%2 == 0:
				continue
			if data[j] in VOWELS and j%2== 1:
				continue
			else:
				result = False
				break
	return result
	
from re import findall, match, split
def checkio2(text):
	isalt = lambda w: ''.join(findall('[AEIOUY]', w)) in (w[0::2], w[1::2])
	words = (w for w in split('\W+', text.upper()) if match('[A-Z]{2,}', w))
	#print( split('\W+',text))
	a = list(filter(isalt, words)) 
	print("a=",a)
	return len(a)
	    
def checkio(text):
	text = text.lower().replace('.',' ').replace(',',' ').split()
	test = text.translate(None, string.punctuation)
	print(text)
	count = 0
	for item in text:
		if IsStripedWords(item) == True:
			count += 1
	return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio2("My name is ...") == 3, "All words are striped"
	assert checkio2("Hello world") == 0, "No one"
	assert checkio2("A quantity of striped words.") == 1, "Only of"
	assert checkio2("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
	checkio2("For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words.")
	checkio2("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?")
		