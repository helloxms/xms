def chase(a1_speed, t2_speed, advantage):
    t = t2_speed*advantage*1.0/(a1_speed - t2_speed)
    #str_t = str(t)
    str_t = "%.8f"%t
    print(str_t)
    
    return str_t

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(chase(6, 3, 2), 4, 8), "example"
    assert almost_equal(chase(10, 1, 10), 11.111111111, 8), "long number"