age = int(input("Enter your age "))
if age >= 18:
    citizenship = input("Are you a citizen")
    if citizenship == "yes":
        Ticket = input("Enter your ticket colour")
        if Ticket == "gold":
            print("VIP louge")
        elif Ticket == "silver":
            print("Main hall")
        elif Ticket == "blue":
            print("Standing area")
        else:
            print("No louge assigned")
    else:
        print("Deny entry")
else:
    print("Deny entry")
