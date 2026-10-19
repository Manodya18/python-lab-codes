d = int(input("Distance travelled"))
f = int(input("Fuel efficiency"))
p = int(input("price per litter"))
h = int(input("Highway charges"))

used = d/f
cost = used*p
final = cost + h

print(used)
print(cost)
print(final)
