prm = input("Is the customer a premium member, Yes/ No")

if prm == "Yes":
    Amount = float(input("Enter purchase amount"))
    if Amount >= 10000:
        print("20% discount applied")
    else:
        print("10% discount applied")
else:
    print("No discount available")
