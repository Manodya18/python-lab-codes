# 1. EVEN NUMBERS 2 TO 20
print("=== 1. EVEN NUMBERS 2 TO 20 ===")
count = 2
while count <= 20:
    print(count)
    count = count + 2

# 2. COUNTDOWN 36 TO 0
print("\n=== 2. COUNTDOWN 36 TO 0 ===")
count = 36
while count >= 0:
    print(count)
    count = count - 6

# 3. COUNTDOWN 25 TO -25
print("\n=== 3. COUNTDOWN 25 TO -25 ===")
count = 25
while count >= -25:
    print(count)
    count = count - 5

# 4. SQUARES 1 TO 10
print("\n=== 4. SQUARES 1 TO 10 ===")
count = 1
while count <= 10:
    print(count*count)
    count = count + 1

# 5. SUM OF NUMBERS - count=0 total=0
print("\n=== 5. SUM OF NUMBERS ===")
count = 0
total = 0
while count <= 10:
    total = total + count
    count = count + 1
print("Total is ", total)
