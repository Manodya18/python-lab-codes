text = input("Enter your string")
i = 0
count = 0

vowels = "AEIOUaeiou"

while i < len(text):
    if text[i] in vowels:
        count = count + 1
    i = i + 1
print(count)
