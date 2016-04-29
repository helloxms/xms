def count_neighbours(grid, row, col):
    height = len(grid)
    wid = len(grid[0])
    rowpos = 0
    colpos = 0
    totalvalue = 0
    for item in grid:
        ll =[]
        if (row - 1 >= 0 and row-1 == rowpos ):
            ll = item          
        if  ( row >=0 and row == rowpos):
            ll = item
        if(row + 1 <= wid-1 and row+1 == rowpos):  
            ll = item
        if ll != []:
            if col-1 >= 0 :
               totalvalue += ll[col-1]
            if col >= 0 and row != rowpos:
                totalvalue += ll[col]
            if col + 1 <= wid-1:
                totalvalue += ll[col+1]
        rowpos += 1
                
        
    
    return totalvalue


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"