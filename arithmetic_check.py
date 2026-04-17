import re
import regular_expressions
arithmeticExprPattern: re.Pattern = re.compile(regular_expressions.arithmeticExprRegex())

def checkArithmeticExpr(arithmeticExpr:str)->bool:
    '''
    arithemetic expression may contain parenthesses and spaces
    operator - arithmetic operator out of +,/,*,-
    operand - any number (may be either fractional or integer, like 10.5, 10)
    check using regular expression (updated from the CW session)
    check pairness of the parenthesses (no regular expression), like (()) - valid, (() -invalid
    '''
    res: bool = False
    if arithmeticExprPattern.fullmatch(arithmeticExpr):
        try:
            __checkPairness(arithmeticExpr)
            res = True
        except:
            pass    
    return res   
def __checkPairness(expr:str):
    count: int = 0
    for ch in expr:
        if ch == "(":
            count += 1
        elif ch == ")":
            count -= 1
        if count < 0: raise Exception() 
    if count != 0: raise Exception() 