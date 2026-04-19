
import operator
import re
import regular_expressions
from arithmetic_check import checkArithmeticExpr
numberRX: str = regular_expressions.numberRegex()
operandsDelimPattern: re.Pattern = re.compile(regular_expressions.operatorRegex())
operatorsDelimPattern: re.Pattern = re.compile(numberRX)
mulDivExpPattern: re.Pattern = re.compile(rf"({numberRX})([*/])({numberRX})")
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
    while mo:=mulDivExpPattern.search(expr):
        op1: float = float(mo.group(1))
        op2: float = float(mo.group(3))
        operation: float = mo.group(2)
        value: float = __binEval(op1, op2 , operation)
        expr = expr[:mo.start()] + str(value) + expr[mo.end():] 
    return expr    
def evaluation(expr: str)->float:
   '''
   evaluation arithmetic expression with assumption:
   no parentheses
   '''
   
   if not checkArithmeticExpr(expr):
       raise ValueError(f"syntax error in expression {expr}")
   expr = re.sub("\s+","",expr) #removing white symbols
   expr = __getExprWithNoMulDiv(expr)
   operands: list[str] = __getOperands(expr)
   operators: list[str] = __getOperators(expr) #first operator is empty string
   result: float = float(operands[0])
   for ind in range(1, len(operands)):
       result = __binEval(result, float(operands[ind]), operators[ind])
   return result   
