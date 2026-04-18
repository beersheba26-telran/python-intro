import re
from regular_expressions import arithmeticRegex, arithmeticRegexParenthereses


def check_parentheses(s: str) -> bool:
    balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0


def checkArithmeticExpr(arithmeticExpr:str)->bool:
    '''
    arithemetic expression may contain parenthesses and spaces
    operator - arithmetic operator out of +,/,*,-
    operand - any number (may be either fractional or integer, like 10.5, 10)
    check using regular expression (updated from the CW session)
    check pairness of the parenthesses (no regular expression), like (()) - valid, (() -invalid
    '''


    if not check_parentheses(arithmeticExpr):
        return False

    def reduce_parens(s: str) -> str:
        paren_E = re.compile(arithmeticRegexParenthereses())
        while True:
            new_s, n = paren_E.subn('X', s)
            if n == 0:
                return s
            s = new_s

    no_paren = arithmeticRegex()

    def is_valid(s: str) -> bool:
        s2 = reduce_parens(s)
        return re.fullmatch(rf'{no_paren}', s2) is not None

    return is_valid(arithmeticExpr)