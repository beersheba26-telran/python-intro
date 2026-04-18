#TODO
def checkArithmeticExpr(arithmeticExpr:str)->bool:
    '''
    arithemetic expression may contain parenthesses and spaces
    operator - arithmetic operator out of +,/,*,-
    operand - any number (may be either fractional or integer, like 10.5, 10)
    check using regular expression (updated from the CW session)
    check pairness of the parenthesses (no regular expression), like (()) - valid, (() -invalid
    '''
