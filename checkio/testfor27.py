import copy
chr_table = []
dict_table={}

def getNextTable( tb ):
	item = tb[0]
	tb.remove(item)
	tb.append(item)
	aa = ''.join( x for x in tb)
	return tb

def initDictTable():
	global chr_table
	global dict_table
	chr_table = [ chr( ord('a')+i) for i in range(0,26) ]
	tb =  copy.copy( chr_table)
	dd={}
	for i in range(0, len(chr_table)):
		str_tb = ''.join(x for x in tb)
		dict_table[ chr_table[i] ] = str_tb
		tb = getNextTable(tb)	

def isRecycleKey( msg, substr):
	for i in range(0, len(msg)):
		if msg[i] != substr[ i%len(substr) ]:
			return False
	return True

def decode_vigenere(old_msg, old_encrypted, new_encrypted):
	global chr_table
	global dict_table
	initDictTable()
	tb =  copy.copy( chr_table)
	origin = old_msg.lower()
	target = old_encrypted.lower()
	new_encrypted = new_encrypted.lower()
	key=[]	
	for i in range(0, len(origin)):
		item = origin[i]
		ss = dict_table.get(origin[i]) 
		for j in range(0, len(ss)):
			if ss[j] == target[i]:
				key.append( chr_table[j] )
				continue
	#get key
	strKey = ''.join(x for x in key)
	for i in range(1, len(strKey)):
		a = strKey[0:i]
		if isRecycleKey(strKey, a):
			strKey = a
			break
	#get origin msg
	new_origin =[]
	for i in range(0, len(new_encrypted) ):
		item = new_encrypted[i]
		key = strKey[i % len(strKey)]
		idx = ord(key)-ord('a')
		for j in range(0, len( chr_table)):
			ss = dict_table[ chr_table[j] ]
			if ss[idx] == item:
				new_origin.append( chr_table[j] )
				
	#return origin msg
	new_origin = ''.join(x for x in new_origin)
	new_origin = new_origin.upper()
	return new_origin

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert decode_vigenere(u'DONTWORRYBEHAPPY',
	                     u'FVRVGWFTFFGRIDRF',
	                     u'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
	assert decode_vigenere(u'HELLO', u'OIWWC', u'ICP') == "BYE", "HELLO"
	assert decode_vigenere(u'LOREMIPSUM',
	                     u'OCCSDQJEXA',
	                     u'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
