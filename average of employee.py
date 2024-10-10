ageList = []  # define a empty list

# receive input from user using a loop to add a list
i = 1
while i <= 5:
    age = int(input("enter age: "))
    ageList.append(age)
    i += 1

# read the list and find average
j = 0
sum = 0
while j < len(ageList):
    sum += ageList[j]
    j += 1
average = sum / len(ageList)

print(f"average is {average}")
