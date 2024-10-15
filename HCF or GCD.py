def hcf(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0:
            result = i
    return result


num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))

print(hcf(num1,num2))

