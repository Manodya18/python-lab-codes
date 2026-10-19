p = float(input("Enter principal amount :"))
i = float(input("Enter your rate :"))
n = int(input("Enter years :"))

investment = p * ((100+i)/100) ** n
interest = investment - p

print("investment is ", investment)
print("interest is ", interest)
