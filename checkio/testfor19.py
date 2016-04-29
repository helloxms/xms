mylist=[]

def check_list(first,second):
	global mylist
	bFindfirst = False
	bFindsecond = False
	for item in mylist:
		if first in item:
			bFindfirst = True
		if second in item:
			bFindsecond = True
	return bFindfirst,bFindsecond	


def add_lists_item(first,second):
	global mylist
	resultv = check_list(first,second)
	bFindfirst = resultv[0]
	bFindsecond = resultv[1]
	if bFindfirst == False and bFindsecond == False:
		mylist.append([first,second])
	if bFindfirst == True and bFindsecond == True:
		for i in range(0,len(mylist)):
			if first in mylist[i]:
				for j in range(0,len(mylist)):
					if second in mylist[j] and i != j:
						mylist[i] = mylist[i]+mylist[j]
						mylist[j] = []
						
						print("here is a combin")
	mylist = [ x for x in mylist if len(x)>0]						
	for item in mylist:
		if first in item and second not in item:
			item.append( second)
		if second in item and first not in item:
			item.append( first)
	
			
	print("affter add:",mylist,first,second)

    

    
def get_relation(first, second):
	global mylist
	print("mylist=",mylist,first,second)
	for item in mylist:
		if first in item and second in item:
			return True
	return False

def check_connection(network, first, second):
	global mylist
	mylist=[]
	print("-------------------check_connection",network,first,second)
	for item in network:
		ls = item.split('-')
		add_lists_item(ls[0],ls[1])
	resultv = get_relation(first, second)
	print("result",resultv)
	return resultv


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert check_connection(
		("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
		"scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
		"scout2", "scout3") == True, "Scout Brotherhood"
	assert check_connection(
		("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
		"scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
		"super", "scout2") == True, "Super Scout"
	assert check_connection(
		("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
		"scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
		"dr101", "sscout") == False, "I don't know any scouts."
	check_connection(("sscout-batman","plane1-scout3","stevan-batman","super-sscout","scout2-batman","scout2-sscout","doc-mega","night-batman","scout3-doc"),"scout2", "plane1")
	assert check_connection(("nikola-robin","batman-nwing","mr99-batman","mr99-robin","dr101-out00","out00-nwing",),"dr101","mr99") == True, "why??"
	