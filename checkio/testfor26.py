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
def checklongword(wordslines,word):
	if len(word)<= 39:
		return word
	slidenum = len(word)//39
	if slidenum > 0 :
		for i in range(0, slidenum ):
			wordslines.append( word[ i*39: (i+1)*39] )
	if len(word)%39 > 0:
		word = word[ slidenum*39:]
		return word
	return ''
	
def getWordsLines(wordslist):
	wordslines=[]
	#get lines
	temp=wordslist[0]
	temp = checklongword(wordslines,temp)
	for i in range(1,len(wordslist)):
		if len(temp)<=39 and len(temp)+1+len(wordslist[i])>39:
			wordslines.append(temp)
			temp=wordslist[i]
			continue
		if temp[-1] != ' ':
			temp = temp + ' '
		temp = temp + wordslist[i]
	if( len(temp)>0):
		print(temp, len(temp))
		temp = checklongword(wordslines,temp)
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
	append1 = ''
	append2 = ''
	if words[0]== ' ':
		append1=' '
	if words[-1] == ' ':
		append2=' '

	words = [ x for x in words.split() if len(x)>0]
	if append1 == ' ':
	    words.insert(0, ' ')
	if append2 == ' ':
	    #words.append(' ')
	  words[-1] = words[-1] +' '
	words= checkio(words)
	print(words)
	return words
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
	expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
	expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
	expected_cowsay_many_lines = r'''
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
'''
	cowsay_one_line = cowsay('Checkio rulezz')
	assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line
	
	cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
	assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines
	
	cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
	                            'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
	assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
	cowsay("spaces                           inside")
	cowsay("looooooooooooooooooooooooooooooooooooong")
	cowsay("loooooooooooooooooooooooooooooooooooong")
	cowsay("looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong")
	cowsay(" a")
	cowsay("b ")
	cowsay(" 0123456789012345678901234567890123456789 ")