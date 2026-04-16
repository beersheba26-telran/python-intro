import re
import regular_expressions

arithmeticExpr = "10+40-90*2/4"
operatorPatern = re.compile(regular_expressions.operatorRegex())

replaced = operatorPatern.sub("<operator>", arithmeticExpr)
print(f'initial text: {arithmeticExpr}')
print(f'replaced text', replaced)

operandPattern = re.compile(regular_expressions.operandRegex())
replaced2 = operandPattern.sub("<operand>", arithmeticExpr)
print(f'replaced operand', replaced2)

