def print_lineFirst(length):

	return "\n "+'_'*length + "\n"
	

def print_lineLast(length):
	return "\n "+'-'*length 

def print_lineTail():
	return r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''	
	
def getWordsLines(wordslist):
	wordslines=[]
	#get lines
	temp=wordslist[0]
	for i in range(1,len(wordslist)):
		if len(temp)<=39 and len(temp)+1+len(wordslist[i])>39:
			wordslines.append(temp)
			temp=wordslist[i]
			continue
		temp = temp +' '+ wordslist[i]
	wordslines.append(temp)
	##
	maxlength = 0
	for i in range(0, len(wordslines)):
		if maxlength <= len(wordslines[i]):
			maxlength = len(wordslines[i])
	#trim print format

	if len(wordslines)>1:
		for i in range(0,len(wordslines)):
			if len(wordslines[i]) <= maxlength:
				wordslines[i] = wordslines[i] + ' '*(maxlength - len(wordslines[i]))
				#print('\n',wordslines[i])
	if len(wordslines)==1:
		wordslines[0] = '< '+wordslines[0] + ' >'
	elif len(wordslines)==2:
		wordslines[0] = '/ '+wordslines[0] + ' \\'
		wordslines[1] = '\\ '+wordslines[1] + ' /'	
	else:
		for i in range(0,len(wordslines)):
			if i== 0:
				wordslines[i] = '/ '+wordslines[i] + ' \\'
			if i>0 and i < len(wordslines)-1:
				wordslines[i] = '| '+wordslines[i] + ' |'
			if i == len(wordslines)-1:
				wordslines[i] = '\\ '+wordslines[i] + ' /'	
			
		
	return wordslines

def print_body(wordslines):
	#print(wordslines)
	
	return '\n'.join(wordslines)
def checkio(words):
		wordslines=getWordsLines(words)
		length = 0
		for i in range(0, len(wordslines)):
			if length <= len(wordslines[i]):
				length = len(wordslines[i])
		length = length -2
		return print_lineFirst(length) + print_body(wordslines) + print_lineLast(length) + print_lineTail()

def cowsay(words):
		words = words.split(' ')
		#print(words)
		words= checkio(words)
		#print(words)
		return words


if __name__ == '__main__':
	assert cowsay('Checkio rulezz') == r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
''' , "Checkio rulezz"

	assert cowsay('A longtextwithonlyonespacetofittwolines.') == r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
''' , "checkio a longtext"
	assert cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.') == r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
''', "check last"