# for addition
def addition(a, b):
    return a + b


# for subtraction
def subtraction(a, b):
    return a - b


# for multiplication
def multiplication(a, b):
    return a * b


# for division
def division(a, b):
    return a / b


while True:
    print('''
press 1 for addition
press 2 for subtraction
press 3 for multiplication
press 4 for division
press 5 for Quit
    ''')

    option = input('enter your operation: ')

    if option == '5':
        print('you have selected Quit, Thank you.')
        break
    if option in ('1', '2', '3', '4'):
        num1 = int(input('enter first number: '))
        num2 = int(input('enter second number: '))
        if option == '1':
            result = addition(num1, num2)
            print(f'result of these numbers are {result}')
        elif option == '2':
            result = subtraction(num1, num2)
            print(f'result of these numbers are {result}')
        elif option == '3':
            result = multiplication(num1, num2)
            print(f'result of these numbers are {result}')
        elif option == '4':
            result = division(num1, num2)
            print(f'result of these numbers are {result}')
    else:
        print('you have entered wrong key')
        continue
