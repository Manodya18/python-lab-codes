b = float(input("Enter basic salary "))
d = int(input("Enter your number of working days "))
t = int(input("Enter extra hours "))

tot = b + (d*(b*0.05)) + t*250
tax = tot * 0.12
salary = tot - tax

print("Salary is ", salary)
