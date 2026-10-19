p = int(input("Room charge per day "))
n = int(input("Number of days "))
f = int(input("Food charges"))
s = int(input("Service charge percentage "))

Subtotal = p*n + f
service = Subtotal*s
final = Subtotal + service

print(Subtotal)
print(service)
print(final)
