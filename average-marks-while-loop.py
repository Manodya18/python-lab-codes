count = 1
total = 0
avg = 0
while (count <= 10):
    mark = int(input("Enter your marks"))
    total = total + mark
    count = count + 1
avg = total/10
print(total)
print(avg)

if avg <50:
    print("Fail")
else:
    print("Pass")
