import re

from regular_expressions import arithmeticRegexParenthereses


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
def evaluateArithmeticExpr(arithmeticExpr: str) -> float:
    if not check_parentheses(arithmeticExpr):
        raise ValueError("Invalid expression")

    def reduce_mul_div(s: str) -> str:
        pattern = re.compile(r'(\d+(?:\.\d+)?)([*/])(\d+(?:\.\d+)?)')
        while True:
            m = pattern.search(s)
            if not m:
                return s
            a, op, b = m.groups()
            a, b = float(a), float(b)
            val = a * b if op == '*' else a / b
            s = s[:m.start()] + str(val) + s[m.end():]

    def reduce_add_sub(s: str) -> str:
        pattern = re.compile(r'(\d+(?:\.\d+)?)([+-])(\d+(?:\.\d+)?)')
        while True:
            m = pattern.search(s)
            if not m:
                return s
            a, op, b = m.groups()
            a, b = float(a), float(b)
            val = a + b if op == '+' else a - b
            s = s[:m.start()] + str(val) + s[m.end():]

    def eval_no_parens(s: str) -> str:
        s = reduce_mul_div(s)
        s = reduce_add_sub(s)
        return s

    def reduce_parens(s: str) -> str:
        paren_E = re.compile(arithmeticRegexParenthereses())
        while True:
            m = paren_E.search(s)
            if not m:
                return s
            inner = m.group(1)
            value = eval_no_parens(inner)
            s = s[:m.start()] + value + s[m.end():]

    try:
        reduced = reduce_parens(arithmeticExpr)
        reduced = eval_no_parens(reduced)
    except Exception:
        raise ValueError("Invalid expression")

    if not re.fullmatch(r'\d+(?:\.\d+)?', reduced):
        raise ValueError("Invalid expression")

    return float(reduced)