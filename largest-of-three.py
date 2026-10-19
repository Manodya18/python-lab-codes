x = int(input("Enter your number 1 "))
y = int(input("Enter your number 2 "))
z = int(input("Enter your number 3 "))

if x > y:
    if x > z:
        print("x is largest ")
    else:
        print("z is largest")
else :
    if y > z:
        print("y is largest")
    else:
        print("z is largest")
