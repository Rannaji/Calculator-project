#Process 1: take input from the user
#input : numbers/operands and operator
operand1 = input('please enter the number 1: ')
operand2 = input('please enter the number 2: ')
operator = input('Enter the operator: ')

#lets check the nature of operands
print(type(operand1), type(operand2))

#changing formats
#type conversion : changing the Data type of one variable to another
operand1 = int(operand1)
operand2 = int(operand2)

#lets check the nature of operands
print(type(operand1), type(operand2))

#lets check the operator First
Result = ''
if operator == '+':
  Result = operand1 + operand2
elif operator == '-':
  Result = operand1 - operand2
elif operator == '*':
  Result = operand1 * operand2
elif operator == '/':
  Result = operand1 / operand2
else:
  Result = 'not defined'

#lets print the result
print('the result is: ',Result)