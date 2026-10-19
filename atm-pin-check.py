pin = input("Enter your pin")
balance = 20000
if pin == "1234":
    amount = int(input("Enter your amount"))
    if amount <= 20000:
        print("Successful")
        print(balance - amount)
    else:
        print("Insufficient balance")
else:
    print("Incorrect pin")
