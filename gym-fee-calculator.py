d = int(input("Monthly fee"))
f = int(input("Number of months"))
p = int(input("Registration fee"))
h = int(input("Personal trainer fee"))

total = d*f + p + h
tax = total * 10
final = total + tax

print(total)
print(tax)
print(final)
