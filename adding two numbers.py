# This is the code for adding two numbers in different methods

# using input from user

# num1 = int(input("enter first number: "))
# num2 = int(input('enter second number: '))
# result = num1 + num2
# print(f'result is {result}')

# using function

# def addNumber(a,b):
#     return a + b
# num1 = 10
# num2 = 20
# result = addNumber(num1,num2)
# print(f'result is {result}')

# using add operator

# import operator
# num1 = 5
# num2 = 7
# result = operator.add(num1,num2)
# print(f'result is {result}')

# using lambda function

addNumber = lambda a,b:a+b
num1 = 8
num2 = 6
result = addNumber(num1,num2)
print(f'result is {result}')