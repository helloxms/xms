import math

def checkbrick( bricks):
	

    for i in range(0, len(bricks)):
        if bricks[i] == '(' and bricks[i+1] == ')':
            bricks[i]= 'a'
            bricks[i+1]= 'a'
            bricks.remove('a')
            bricks.remove('a')
            break
        if bricks[i] == '[' and bricks[i+1] == ']':
            bricks[i]= 'a'
            bricks[i+1]= 'a'
            bricks.remove('a')
            bricks.remove('a')
            break
        if bricks[i] == '{' and bricks[i+1] == '}':
            bricks[i]= 'a'
            bricks[i+1]= 'a'
            bricks.remove('a')
            bricks.remove('a')
            break
            
    return bricks
    
def checkio(expression):
    bricks=[]
    dictFlag={}
    brick_table=['(', ')', '[', ']', '{', '}' ]
    dictFlag['('] = 0
    dictFlag[')'] = 0
    dictFlag['['] = 0
    dictFlag[']'] = 0
    dictFlag['{'] = 0
    dictFlag['}'] = 0
    

    for item in expression:
       if item in brick_table:
					dictFlag[item] +=1;
					bricks.append(item)
					#print(bricks)           

    if bricks == [] :
        return True
    if dictFlag['('] != dictFlag[')'] :
        return False
    if dictFlag['['] != dictFlag[']'] :
        return False
    if dictFlag['{'] != dictFlag['}'] :
        return False        
    totalcount = dictFlag['('];
    totalcount += dictFlag['['];
    totalcount += dictFlag['{'];
    #print("totalcount=" , totalcount)
    pos = 0
    for i in range(0, totalcount ):
        bricks = checkbrick(bricks)
        #print("bricks=",bricks)
        if( bricks == None):
        	break
   
            
    if bricks == [] :
        return True;
        
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
