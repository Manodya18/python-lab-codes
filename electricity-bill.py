while True:
    units = int(input("Enter your consume units"))

    if units > 60:
        charge = 30*20 + 30*40 + (units-60)*60
    elif units > 30:
        charge = 30*20 + (units-30)*40
    else:
        charge = units*20

    print(charge)
