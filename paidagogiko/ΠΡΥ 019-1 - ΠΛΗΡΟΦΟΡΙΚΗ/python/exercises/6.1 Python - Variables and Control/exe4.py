# Άσκηση 4: ο μικρότερος από τρεις ακεραίους

x = int(input("Dose enan arithmo x: "))
y = int(input("Dose enan arithmo y: "))
z = int(input("Dose enan arithmo z: "))

smallest = x
if y < smallest:
    smallest = y
if z < smallest:
    smallest = z

print(f"{smallest} is the smallest")
