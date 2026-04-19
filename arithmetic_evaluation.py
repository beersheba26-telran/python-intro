
import operator
import re
import regular_expressions
from arithmetic_check import checkArithmeticExpr
numberRX: str = regular_expressions.numberRegex()
operandsDelimPattern: re.Pattern = re.compile(rf"(?<=\d){regular_expressions.operatorRegex()}") #5+-20 - operands 9, -20
operatorsDelimPattern: re.Pattern = re.compile(rf"(?<!\d)-?{numberRX}") #5+-20 - operators "", "+" (- won't be operator, as - will be a part of delimiter)
mulDivExpPattern: re.Pattern = re.compile(rf"({numberRX})([*/])({numberRX})")
expInsideParenthesesPattern: re.Pattern = re.compile(r"\([^()]+\)")
ops: dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
def __getOperands(expr: str):
   return operandsDelimPattern.split(expr)
def __getOperators(expr: str):
    return operatorsDelimPattern.split(expr)
   
def __binEval(op1: float, op2: float, operation: str)->float: 
    '''
    returns result of binary operation
    '''
    try:
        return ops[operation](op1, op2)
    except KeyError as e:
        raise ValueError(f"operation {operation} not implemented yet")
def __getExprWithNoMulDiv(expr: str)->str: 
    '''
    returns original expression but with no multiplication and division operations
    sequential in line loop sustitution of mulDivExpPattern with results of single multiplication/division operations
    '''
    
    while mo:=mulDivExpPattern.search(expr):
        op1: float = float(mo.group(1))
        op2: float = float(mo.group(3))
        operation: float = mo.group(2)
        value: float = __binEval(op1, op2 , operation)
        expr = expr[:mo.start()] + str(value) + expr[mo.end():] 
    return expr    
def __evaluationNoParentheses(expr: str)->float:
   '''
   evaluation arithmetic expression with :
   no parentheses
   '''
   while mo := re.search(r"\([^()]+\)", expr):
        inner = mo.group()[1:-1]  # removing ()
        value = __evaluationNoParentheses(inner)
        expr = expr[:mo.start()] + str(value) + expr[mo.end():]
  
   expr = __getExprWithNoMulDiv(expr)
   operands: list[str] = __getOperands(expr)
   operators: list[str] = __getOperators(expr) #first operator is empty string
   result: float = float(operands[0])
   for ind in range(1, len(operands)):
       result = __binEval(result, float(operands[ind]), operators[ind])
   return result   
def __getExprWithNoParentheses(expr: str) -> float:
    '''
    returns expression containing values sequentionally evaluated inside perentheses
    '''
    
    while mo := expInsideParenthesesPattern.search( expr):
        inner = mo.group()[1:-1]  # removing ()
        value = __evaluationNoParentheses(inner)
        expr = expr[:mo.start()] + str(value) + expr[mo.end():]
    return expr    
def evaluation(expr: str)->float:
    '''
    entry point to the evaluation of expression with parentheses taking in the consideration operation
    preferences
    '''
    
    if not checkArithmeticExpr(expr):
       raise ValueError(f"syntax error in expression {expr}")
    expr = re.sub("\s+","",expr) #removing white symbols
    expr = __getExprWithNoParentheses(expr)
    return __evaluationNoParentheses(expr)
    
