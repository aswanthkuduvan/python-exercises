# a = 20
# b = 15
# temp = a
# a = b
# b = temp
# print(f'value in a is {a}, value of b is {b}')

# without extra variable

a = 20
b = 15
a, b = b, a
print(f'value in a is {a}, value of b is {b}')
