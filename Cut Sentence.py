""" Your task in this mission is to truncate a sentence to a length, 
that does not exceed a given number of characters.

If the given sentence already is short enough you don't have to do anything to it, 
but if it needs to be truncated the omission must be indicated by 
concatenating an ellipsis ("...") to the end of the shortened sentence.

The shortened sentence can contain complete words and spaces.
It must neither contain truncated words nor trailing spaces.
The ellipsis has been taken into account for the allowed number of
 characters, so it does not count against the given length.

Input: Two arguments:

    one-line sentence as a string
    max length of the truncated sentence as an int

Output: The shortened sentence plus the ellipsis (if required) as a one-line string.

Precondition:

    line.startswith(' ') == False
    0 < len(line) ≤ 79
    0 < length ≤ 76
    all(char in string.ascii_letters + ' ' for char in line)"""
    
def cut_sentence(line, length):
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    
    if len(line) <= length: # the whole sentence fits in the given length
        return line
    # if the truncated sentence contains only full words or no words at all
    if line[length] == ' 'or length == 0:    
        return line[:length]+"..."
    else:
        # reduce length by 1 and try again
       return cut_sentence(line,length-1)

