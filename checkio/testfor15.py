class Friends:
	_mylist=[]
	_dict={}
	_names=()
	
	def __init__(self, connections):
		self._mylist=[]
		self._dict={}
		self._names=()
		for item in connections:
			f1 = item.pop()
			f2 = item.pop()
			self._mylist.append(f1)
			self._mylist.append(f2)
			if f1 not in self._dict:
				self._dict[f1] = []
			self._dict[f1].append(f2)
			if f2 not in self._dict:
				self._dict[f2] = []
			self._dict[f2].append(f1)
			print("\n\ninit",self._dict)
            

	def add_init(self, f1):
		if f1 not in self._dict:
			self._dict[f1] = []
		print("add_init",f1,self._dict)   
        
	def add_connect(self, f1, f2):
		self.add_init(f1)
		self.add_init(f2)
		if f1 in self._dict:
			self._dict[f1].append(f2)
		if f2 in self._dict:
			self._dict[f2].append(f1)
		print("add_connect",f1,f2, self._dict )
            
	def has_connect(self, f1,f2):
		if f1 in self._dict and self._dict[f1].count(f2)>0 :
			print("has_connect true",f1,f2, self._dict[f1])
			return True
		print("has connect false")
		return False
        
	def add(self, connection):
		f1 = connection.pop()
		f2 = connection.pop()
		print("add",f1,f2,self._dict)
		if self.has_connect(f1,f2) == True:
			return False
		self.add_connect(f1,f2)
		print("after add",f1,f2,self._dict)
		return True

	def remove(self, connection):
		f1 = connection.pop()
		f2 = connection.pop()
		print("remove",f1,f2)
		print("befor remove",f1,f2,self._dict)
		if f1 in self._dict and f2 in self._dict:
			L = self._dict[f1]
			L = filter(lambda x:x!= f2, L)
			self._dict[f1] = L
			L = self._dict[f2]
			L = filter(lambda x:x!= f1, L)
			self._dict[f2] = L
			print("after remove",f1,f2,self._dict)
			return True
		return False
        
	def names(self):
		self._names =set( self._dict.keys())
		print("names",self._names)
		ff=[]
		for item in self._names:
			if len(self._dict[item])>0:
				ff.append(item)
		print("names",ff)
		return set(ff)
        
	def connected(self, name):
		if name not in self._dict:
			return set()		
		print("connected name:",name,self._dict)
		print("connected name:",name, set(self._dict[name] ))
		if name in self._dict and len(self._dict[name]) > 0:
			return set(self._dict[name])
		return set()



if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
	digit_friends = Friends([{"1", "2"}, {"3", "1"}])
	assert letter_friends.add({"c", "d"}) is True, "Add"
	assert letter_friends.add({"c", "d"}) is False, "Add again"
	assert letter_friends.remove({"c", "d"}) is True, "Remove"
	assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
	assert letter_friends.names() == {"a", "b", "c"}, "Names"
	assert letter_friends.connected("d") == set(), "Non connected name"
	assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
	f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"})) 
	f.remove({"stephen", "robot"}) 
	f.names()
	f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"})) 
	f.connected("DDD")