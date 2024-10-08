num = int(input('enter number: '))
result = list(map(lambda x:x**2,range(num+1)))

for i in range(num+1):
    print(result[i])