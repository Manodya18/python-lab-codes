prm = int(input("Press 1 if you are a premium/ press 0 otherwise"))

if prm == 1:
    Amount = float(input("Enter purchase amount"))
    if Amount >= 10000:
        dis = Amount * 20/100
        print("20% discount applied", dis)
    else:
        dis = Amount * 10/100
        print("10% discount applied", dis)
else:
    print("No discount available")
