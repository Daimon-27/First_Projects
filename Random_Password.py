import random

def random_lower_letter():
    return chr(random.randint(ord('a'), ord('z')))


def random_upper_letter():
    return chr(random.randint(ord('A'), ord('Z')))


def random_number():
    return str(random.randint(0, 9))


def random_symbol():
    return random.choice(symbols)

while True:
    try:
        password_length = int(input('Введіть довжину пароля 6-32 символи: '))
        if str(password_length) == 'stop':
            break
        elif password_length not in range(6, 33):
            print('Введіть ціле число в межах від 6 до 32!')
            break

        password = ''
        symbols = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=')

        for i in range(password_length):
            all_methods = (random_lower_letter(), random_upper_letter(), random_number(), random_symbol())
            password = password + random.choice(all_methods)
        print(password)
    except ValueError:
        print('Введіть число, а не символ!')