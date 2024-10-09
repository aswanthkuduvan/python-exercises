start = int(input('enter starting number: '))
end = int(input('enter ending number: '))

for num in range(start,end+1):
    length = len(str(num))
    result = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        result += digit ** length
        temp //= 10
    if result == num:
        print(num)