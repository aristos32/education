# Άσκηση 5: γραμμές, χαρακτήρες, γράμματα, ψηφία, ειδικοί, λέξεις. Ένα open-close.

name = input("Enter file name to read: ")

f = open(name)
lines = 0
words = 0
letters = 0
numbers = 0
special = 0
total = 0

for line in f:
    lines = lines + 1
    words = words + len(line.split())
    for c in line:
        if c == "\n":
            continue
        total = total + 1
        if c.isalpha():
            letters = letters + 1
        elif c.isdigit():
            numbers = numbers + 1
        else:
            special = special + 1
f.close()

print()
print("File Status")
print("===========")
print()
print("Words: ", words)
print("Characters: ", letters)
print("Numbers: ", numbers)
print("Special Characters: ", special)
print("Total Characters: ", total)
print("Lines: ", lines)
