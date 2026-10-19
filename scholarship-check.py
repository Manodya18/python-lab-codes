A = float(input("Enter your attendance "))

if A >= 80:
    M = float(input("Enter your marks "))
    if M >= 75:
        print("Scholarship Awarded")
    else :
        print("Scholarship not Awarded")
else:
    print("Insufficient Attendance")
