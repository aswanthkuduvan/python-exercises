number = [2, 5, 6, 7, 1, 8, 9]
odd = []

i = 0
while i < len(number):
    if number[i] % 2 == 1:
        odd.append(number[i])
    i += 1
print(odd)