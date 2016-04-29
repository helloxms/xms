
def get_cost(data):
    cost = 0
    doubleFlag = False
    sumv = 0
    sumleft = 0
    for item in data:        
        if( doubleFlag == False):            
            sumv += item
        if(sumv > 100 and doubleFlag == False):
            doubleFlag = True
            sumleft = sumv-100
            sumv = 100
            continue
        if(doubleFlag == True):
            sumleft += item
    print("sumv=", sumv,"sumleft=", sumleft)
    cost = sumv + sumleft*2
    return cost
            
def total_cost(calls):
    mydict = {}
    for item in calls:        
        mysplit = item.split()
        mydict[mysplit[0]] = []
    for item in calls:        
        mysplit = item.split()
        curtime = int(mysplit[2])
        if( curtime%60 == 0):
            curtime = curtime//60
        else:
            curtime = curtime//60 + 1
        mydict[mysplit[0]].append(curtime)
    print(mydict)
    mycost=[]
    for k,v in mydict.items():
        mycost.append( get_cost(v))
    print(mycost)
    return sum(mycost)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"