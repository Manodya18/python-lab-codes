salary = int(input("Enter your salary"))
if salary >= 50000:
    credit = int(input("Enter your credit score"))
    if credit >= 700:
        print("Loan Approved")
    else:
        print("Credit score is not enough")
else:
    print("Salary is not enough")
