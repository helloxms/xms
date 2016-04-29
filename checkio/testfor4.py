def letter_queue(commands):
    myque=[]
    for item in commands:
        if item.find("PUSH") == 0 :
            s = item.split()
            char = s[1]
            myque.append(char)
            #print(myque)
        if item.find("POP")== 0 and myque != []:            
            myque.remove(myque[0])
            #print(myque)
    str_convert = ''.join(myque)
    return str_convert

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"