num1 = float(input('Введіть перше число:'))
num2 = float(input('Введіть друге число:'))
operation = input('Ведіть арифметичну дію +, -, *, або /:')

def get_sum(a, b):
    print(a + b)

def get_difference(a, b):
    print(a - b)

def get_product(a, b):
    print(a * b)

def get_fraction(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('На нуль ділити не можна!')

if  operation == '+':
    get_sum(num1, num2)
elif operation == '-':
    get_difference(num1, num2)
elif operation == '*':
    get_product(num1, num2)
else:
    get_fraction(num1, num2)