#python calculator
operator = input('enter an operator (+ - /):')
num1 = float(input('enter the 1st value: '))
num2 = float(input('enter the 2nd value: '))

result = 0

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1-num2
elif operator == '/':
    result = num1/num2
elif operator == '*':
    result = num1*num2
else:
    print(f'{operator} is not a valid operator')

print(round(result,3))
