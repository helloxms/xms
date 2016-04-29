import string

def remove_punctuation(msg):
		#out = msg.translate(string.maketrans("",""), string.punctuation)
		#return out
	mylist = list(msg)
	myresult =[]
	for item in mylist:
		if item.isalpha() or item.isspace():
			myresult.append(item)
	
	return ''.join(myresult)		

def getLikenessValue(word1, word2):
		value = 0.0
		lens1 = len(word1)
		lens2 = len(word2)
		combinword = word1 + word2
		common_letter = []
		for item in word1:
			if item in word2:
				common_letter.append(item)
		myset1 = set(common_letter)		
		myset2 = set(combinword)

		if word1[0] == word2[0] :
			value += 10.0
		if word1[lens1-1] == word2[lens2-1]:
			value += 10.0
		if lens1>lens2:
			value  += (lens2*30.0 / lens1)
		elif( lens1 <= lens2):
			value += (lens1*30.0  / lens2)
		
		value += (len(myset1)*50.0/len(myset2) )
		
		return value
		
def find_word(message):
		msg = message.lower()
		msg = remove_punctuation(msg)
		filtermsg_row = msg.split()
		filtermsg_col = filtermsg_row

		row_values =[]
		max_row_value = 0;
		max_row_pos = 0;
		for i in range(0, len(filtermsg_row)):
			cur_row_value = 0.0
			for j in range(0, len(filtermsg_col)):
				if i != j:
					cur_row_value += getLikenessValue( filtermsg_row[i], filtermsg_col[j])
			
			row_values.append(cur_row_value)
			if max_row_value <= cur_row_value:
				max_row_value = cur_row_value
				max_row_pos = i
		
		print(filtermsg_row)
		print("row_values", row_values)
		print("max_row_value", max_row_value)
		print("max_row_pos", max_row_pos)
		print(filtermsg_row[max_row_pos])
							
		return filtermsg_row[max_row_pos]
		


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"