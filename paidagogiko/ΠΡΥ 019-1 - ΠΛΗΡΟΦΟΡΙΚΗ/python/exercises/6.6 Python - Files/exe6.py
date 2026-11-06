# Άσκηση 6: άθροισμα των x και των y από το xy.txt

sum_x = 0
sum_y = 0

f = open("xy.txt")
for line in f:
    parts = line.split()
    value = float(parts[1])
    if parts[0] == "x=":
        sum_x = sum_x + value
    else:
        sum_y = sum_y + value
f.close()

print(f"Το άθροισμα των x είναι {sum_x}")
print(f"Το άθροισμα των y είναι {sum_y}")
