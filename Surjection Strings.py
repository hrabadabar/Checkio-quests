"""Maybe it's a cipher? Maybe, but we don’t know for sure.

Maybe you can call it "homomorphism"? i wish I know this word before.

You need to check that the 2 given strings are isometric. 
This means that a character from one string can become a match for characters from another string.

One character from one string can correspond only to one character 
from another string. Two or more characters of one string can correspond 
to one character of another string, but not vice versa.

Input: Two arguments. Both strings.

Output: Boolean.

Precondition:
both strings are the same size """

def isometric_strings(str1: str, str2: str) -> bool:
    
	dic = {}
	for j in range(len(str1)):
		x = str1[j]
		y = str2[j]
	# check if one to one mapping is possible	
		if x in dic:
			if dic[x] != y:   # already mapped to another chacarter
				return False
		
		
		dic[x] = y
	
	return True
			


