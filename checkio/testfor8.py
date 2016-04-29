
#a(x1,y1) b(x2,y2) c(x3,y3)

# line ab -> line r
# slope mr = (y2-y1)/(x2-x1)
# yr - y1 = mr*( x - x1)
# yr = mr*( x -x1) + y1

#line bc -> line t
#slop mt = (y3 -y2)/(x3-x2)
# yt -y2 = mt*(x -x2)
# yt = mt*(x -x2) + y2

# 2line -> center point
# Centerx = ( mr*mt*(y3-y1) + mr*(x2+x3) - mt(x1+x2) )/ 2*(mr - mt)
# Centery = (-1/mr)*(x - (x1+x2)/2) + (y1+y2)/2
# R = sqrt( (x1 - Centerx)^2 + (y1 - Centery)^2 )

import math

def getPointValue( strPoint):
	strPoint = strPoint.replace('(','')
	strPoint = strPoint.replace(')','')
	point = strPoint.split(',')
	value =[]
	value.append( float(point[0]) )
	value.append( float(point[1]) )
	return value
		

def getPoints(strData):
	strData = strData.replace("),", ");")
	strData = strData.split(';')
	assert len(strData) == 3
	point1 = getPointValue( strData[0] )
	point2 = getPointValue( strData[1] )
	point3 = getPointValue( strData[2] )
	return point1+point2+point3
				
def trimResult(strvalue):
	if(strvalue.find('.')> 0 and strvalue[len(strvalue)-1] == '0'):
		tmp = strvalue[::-1]
		trimpos = 0
		for i in range(0, len(tmp)):
			if tmp[i] == '0':
				trimpos += 1
			else:
				break
		if trimpos > 0:
			strvalue = strvalue[0: len(strvalue)-trimpos]
		
		if strvalue[len(strvalue)-1] == '.':
			strvalue=strvalue.replace('.','')
	
	return strvalue
	
def getcenter(data):
	
	points = getPoints(data)
	x1 = points[0]
	y1 = points[1]
	x2 = points[2]
	y2 = points[3]
	x3 = points[4]
	y3 = points[5]
	print( points)
    #make sure x2 != x1 and x3 != x2
	if( x2 - x1 == 0 ):
		tmpx = x2
		tmpx = y2
		x2 = x3
		y2 = y3
		x3 = tmpx
		y3 = tmpx
	elif( x3 - x2 == 0):
		tmpx = x2
		tmpy = y2
		x2 = x1
		y2 = y1
		x1 = tmpx
		y1 = tmpx
 
	mr = (y2 - y1)*1.0/(x2 - x1)
	mt = (y3 - y2)*1.0/(x3 - x2)
	print( "mr=", mr, " mt=",mt)# 0 -1
	cx = ( mr*mt*(y3-y1) + mr*(x2+x3) - mt*(x1+x2) )*0.5/ (mr - mt)

	if mr != 0:
		cy = (-1.0/mr)*(cx - (x1+x2)/2.0) + (y1+y2)/2.0
	elif mt != 0:
		cy =  (-1.0/mt)*(cx - (x2+x3)/2.0) + (y2+y3)/2.0
	
	r = math.sqrt( math.pow( x1 - cx, 2) + math.pow( y1 - cy, 2) )
	cx = "%.2f"%(cx)
	cy = "%.2f"%(cy)
	r = "%.2f"%(r)
	cx = trimResult(cx)
	cy = trimResult(cy)
	r = trimResult(r)
	return cx,cy,r
    
    
def checkio(data):
		result = getcenter(data)
		print("result=", result )
		value = "(x-cx)^2+(y-cy)^2=R^2"
		value = value.replace("cx", str(result[0]))
		value = value.replace("cy", str(result[1]))
		value = value.replace("R", str(result[2]))
		print( value)
		return value

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    print( checkio(u"(9,4),(9,8),(3,6)") )