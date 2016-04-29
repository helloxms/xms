class Building:
	_p0 = 0.0
	_p1 = 0.0
	_width_WE = 0.0
	_width_NS = 0.0
	_height = 0.0
	_corners={}   
	#_corners={"north-west":[0,0],"north-east":[0,0],"south-west":[0,0],"south-east":[0,0]}
	_area = 0.0
	_volume = 0.0
	
	def __init__(self, south, west, width_WE, width_NS, height=10):
		self._p0 = south
		self._p1 = west
		self._width_WE = width_WE
		self._width_NS = width_NS
		self._height = height
		self._area = self._width_WE*self._width_NS
		self._volume = self._area*self._height
		self._corners["north-west"]= [self._p0 + self._width_NS, self._p1]
		self._corners["north-east"]= [self._p0 + self._width_NS, self._p1+self._width_WE]
		self._corners["south-west"]= [self._p0, self._p1]
		self._corners["south-east"]= [self._p0, self._p1 + self._width_WE]   	
		print("end of init")	
		print( south, west)
    #print(str( self._p0), str(self._p1), str(self._area), str(self._volume) ) )
    
	def corners(self):
		return self._corners

	def area(self):
		return self._area

	def volume(self):
		return self._volume

	def trimnum(self, num):
		ss = str(num)
		return ss

	def __repr__(self):
		
		strbuild = "Building(%s, %s, %s, %s, %s)"%(self.trimnum(self._p0), self.trimnum(self._p1), 
		self.trimnum(self._width_WE), self.trimnum(self._width_NS), self.trimnum(self._height) )
		return strbuild


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
	def json_dict(d):
		return dict((k, list(v)) for k, v in d.items())

	b = Building(1, 2, 2, 3)
	b2 = Building(1, 2, 2, 3, 5)
	assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
	                                  'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
	assert b.area() == 6, "Area"
	assert b.volume() == 60, "Volume"
	assert b2.volume() == 30, "Volume2"
	print(str(b) )
	assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
	print( str(Building(0.2,1,2,2.2,3.5)) )
	
	