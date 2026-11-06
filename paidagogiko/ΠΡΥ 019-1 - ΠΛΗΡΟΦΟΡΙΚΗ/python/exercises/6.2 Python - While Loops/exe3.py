# Άσκηση 3: μικρότερος και μεγαλύτερος, τερματισμός με -1

n = int(input("Give a number: "))
smallest = n
largest = n

while n != -1:
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n
    n = int(input("Give a number: "))

print(f"{smallest} is the smallest")
print(f"{largest} is the largest")
