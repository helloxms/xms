
def flat_list(a):
    b=str(a).replace('[',' ').replace(']',' ').replace(',',' ').split()
    return  [int(i) for i in b]
 


if __name__ == '__main__':
	print( flat_list([1,2,3]) )
	print( flat_list([[]])  )
	print( flat_list([20,-10,[[[]]]] ) )

