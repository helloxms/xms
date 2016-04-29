def undersafe(pawn, pawns):
	result = False
	for item in pawns:
		if int(item[1]) == int(pawn[1])-1 :
			if (ord(item[0]) == ord(pawn[0])-1 or ord(item[0]) == ord(pawn[0])+1):
				print( "safe:", pawn, item)
				return True
	return result
        
def safe_pawns(pawns):
    count = 0
    for item in pawns:
        if undersafe(item, pawns) == True:
            count += 1    
    print("safe count=",count)
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1