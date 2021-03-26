""" You have a text and a list of words. You need to check if the words 
in a list appear in the same order as in the given text.

Cases you should expect while solving this challenge:

a word from the list is not in the text - your function should return False;
any word can appear more than once in a text - use only the first one;
two words in the given list are the same - your function should return False;
the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
the text includes only English letters and spaces.

Input: Two arguments. The first one is a given text, the second is a list of words.

Output: A bool. """

def words_order(text: str, words: list) -> bool:
    # check if every word in words is also present in text
    if all(words[x] in text.split() for x in range(len(words))):
            # note where in text each word from words appear
            indices = [text.split().index(x) for x in words] 
            
            if len(indices) == 1: # only one word in words
                return True
            # check if indices is sorted in ascending order and 
            # if it is already a set and words contain no duplicates
            if len(indices) > 0 and sorted(set(indices)) == indices:
                return True
    return False
