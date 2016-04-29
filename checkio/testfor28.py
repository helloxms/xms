a_factaral=f=lambda x:max(1,x and x*f(x-1))
if __name__ == '__main__':
    assert a_factaral(0) == 1, "0"
    assert a_factaral(1) == 1, "1"
    assert a_factaral(2) == 2, "2"
    assert a_factaral(3) == 6, "6"
    assert a_factaral(100) == \
           93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, "Infinity"
