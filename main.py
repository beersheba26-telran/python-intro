import re
import regular_expressions
arithmeticExpr:str = "10+40-90*2/4"
operatorPattern: re.Pattern = re.compile(regular_expressions.operatorRegex())
operandPattern: re.Pattern = re.compile(regular_expressions.operandRegex())
replaced:str = operatorPattern.sub("<operator>",arithmeticExpr)
print(f"initial text is {arithmeticExpr}; replaced is {replaced}")
replaced = operandPattern.sub("<operand>", arithmeticExpr)
print(f"initial text is {arithmeticExpr}; replaced is {replaced}")
operators: list[str] = operandPattern.split(arithmeticExpr)
print("operators ", operators)