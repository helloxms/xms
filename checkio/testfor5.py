import math


    #a=[sum(x) for x in matrix]
    #b=[sum([row[i] for row in matrix]) for i in range(len(matrix))]
    
    #return a.index(min(a)), b.index(min(b))  # [0, 0]
    
    
def weak_point(matrix):
    
    mydict={}
    rowvaluelist = []
    colvaluelist = []
    rowvalue = 0        
    colvalue = 0
    

    for i in range(0, len(matrix) ):        
        rowvalue = 0
        for j in range(0, len(matrix) ):
            rowvalue += matrix[i][j]
        rowvaluelist.append( rowvalue)
        
        
    for i in range(0, len(matrix) ):
        colvalue = 0
        for j in range(0, len(matrix) ):
            colvalue += matrix[j][i]
        colvaluelist.append( colvalue)
        
        
    #print( rowvaluelist)
    #print( colvaluelist)
    currowvalue = rowvaluelist[0]
    curcolvalue = colvaluelist[0]
    mincolpos = 0
    minrowpos = 0        
    for i in range(0, len(rowvaluelist) ):
        if currowvalue > rowvaluelist[i]:
            minrowpos = i
            currowvalue = rowvaluelist[i]
    
    for i in range(0, len(colvaluelist) ):
        if curcolvalue > colvaluelist[i]:
            mincolpos = i
            curcolvalue = colvaluelist[i]
    
    return minrowpos,mincolpos  # [0, 0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"