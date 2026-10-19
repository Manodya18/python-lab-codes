while True:
    emp = int(input("Enter your employee's performance"))

    if emp >= 85:
        yos = int(input("Enter your years of service"))
        if yos >= 3:
            print("Promotion Approved")
        else:
            print("More experience required")
    else:
        print("Performance Improvement Required")
