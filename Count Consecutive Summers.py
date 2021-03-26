""" Positive integers can be expressed as sums of consecutive positive integers in various ways. 
For example, 42 can be expressed as such a sum in four different ways:
(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42. 
As the last solution (d) shows, any positive integer can always be 
trivially expressed as a singleton sum that consists of that integer alone.

Compute how many different ways it can be expressed as a sum of consecutive positive integers.

Input: Int.

Output: Int.

Precondition: Input is always a positive integer.

The mission was taken from Python CCPS 109 Fall 2018. 
It’s being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen"""

import math
def count_consecutive_summers(num):
    count = 1
    # divide the integer by 2 and add 1. You don't need to
    # check further than that. 
    for j in range(1,math.ceil(num/2)+1): # for each integer from 2 to num
        if num != 1:    
            k = j   # note the current integer
            res = 0 # the sum so far is 0
            while res < num:  # until the sum so far is smaller than num
                res += k      # add current integer to the sum
                k += 1      # and check with next number
                if res == num:  # else
                    count += 1  # increase count
        else: return count
        
        
            
    return count


