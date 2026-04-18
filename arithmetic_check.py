import re
from regular_expressions import arithmeticRegex, arithmeticRegexParenthereses

def checkArithmeticExpr(arithmeticExpr:str)->bool:
    '''
    arithemetic expression may contain parenthesses and spaces
    operator - arithmetic operator out of +,/,*,-
    operand - any number (may be either fractional or integer, like 10.5, 10)
    check using regular expression (updated from the CW session)
    check pairness of the parenthesses (no regular expression), like (()) - valid, (() -invalid
    '''

    def reduce_parens(s: str) -> str:
        paren_E = re.compile(arithmeticRegexParenthereses())
        while True:
            new_s, n = paren_E.subn('X', s)  # X — новый атом
            if n == 0:
                return s
            s = new_s
    no_paren = arithmeticRegex()
    def is_valid(s: str) -> bool:
        s2 = reduce_parens(s)
        return re.fullmatch(rf'{no_paren}', s2) is not None

    return is_valid(arithmeticExpr)