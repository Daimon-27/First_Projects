num1 = float(input('Введіть перше число: '))
operation = input('Ведіть арифметичну дію +, -, *, /, %, ^: ')
num2 = float(input('Введіть друге число або до якого степення треба піднести перше число: '))

def get_sum(input_num1, input_num2):
    print('Сума: ', input_num1 + input_num2)

def get_difference(input_num1, input_num2):
    print('Різниця: ', input_num1 - input_num2)

def get_product(input_num1, input_num2):
    print('Добуток: ', input_num1 * input_num2)

def get_fraction(input_num1, input_num2):
    try:
        print('Частка: ', input_num1 / input_num2)
    except ZeroDivisionError:
        print('На нуль ділити не можна!')

def get_remainder_from_division(input_num1, input_num2):
    print('Залишок від ділення: ', input_num1 % input_num2)

def get_exponentiation(input_num1, input_num2):
    print(f'Піднесення до {int(input_num2)} степення: ', input_num1 ** input_num2)

if  operation == '+':
    get_sum(num1, num2)
elif operation == '-':
    get_difference(num1, num2)
elif operation == '*':
    get_product(num1, num2)
elif operation == '/':
    get_fraction(num1, num2)
elif operation == '%':
    get_remainder_from_division(num1, num2)
else:
    get_exponentiation(num1, num2)