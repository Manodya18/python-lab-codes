count = 0
largest = 0
while count <5:
    num = int(input("Enter your number "))
    if largest < num:
        largest = num
    else:
        largest = largest

    count = count + 1
print(largest)
