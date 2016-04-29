def longest_palindromic(text):

    str = "#" + "#".join(text) + "#"
    #print str
    i = 0
    mx = 0
    id = 0
    p = [0 ] * len(str)
    while i<len(str):
        if mx > i:
            p[i] = min(p[ 2*id-i],mx-i)
        else:
            p[i] = 1
     
        while i-p[i] >=0 and i+p[i] < len(str) and str[i-p[i]]==str[i+p[i]]:
            p[i] += 1
     
        if mx < p[i]+i:
            mx = p[i] + i
            id = i
        i+=1    
    return text

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"