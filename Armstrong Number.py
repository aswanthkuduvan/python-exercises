num = int(input('enter number: '))
result = 0
temp = num
length = len(str(num))

while temp > 0:
    digit = temp % 10
    result += digit ** length
    temp //= 10

if result == num:
    print('Armstrong number')
else:
    print('Not armstrong')