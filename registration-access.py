registration = input("Are you registered")
if registration == "yes":
    fee = input("Did you paid the registration fee")
    if fee == "yes":
        print("Can Access")
    else:
        print("Can't access")
else:
    print("Can't access")
