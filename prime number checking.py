num = int(input("enter number: "))
i = 2

while i < num:
    if num % i == 0:
        print("not prime")
        break
    i += 1

else:
    print("prime number")