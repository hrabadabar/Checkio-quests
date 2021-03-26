""" You are given an expression with numbers, brackets and operators. 
For this task only the brackets matter. Brackets come in three flavors: 
"{}" "()" or "[]". Brackets are used to determine scope or to restrict 
some expression. If a bracket is open, then it must be closed with a 
closing bracket of the same type. The scope of a bracket must not 
intersected by another bracket. In this task you should make a decision, 
whether to correct an expression or not based on the brackets. Do not 
worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).

Precondition:
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
0 < len(expression) < 103 """

def checkio(expression):
    brackets1 = '([{'
    brackets2 = ')]}'
    f = []
    for c in expression:
        if c in brackets1:
            f.append(c)
        elif c in brackets2:
            if len(f) == 0:      # no bracket to match   
                return False
            # each left bracket should be matched by the corresponding right bracket
            if brackets2.index(c) != brackets1.index(f.pop()):
                return False
    # there shouldn't be any unmatched brackets left
    return len(f) == 0
            

