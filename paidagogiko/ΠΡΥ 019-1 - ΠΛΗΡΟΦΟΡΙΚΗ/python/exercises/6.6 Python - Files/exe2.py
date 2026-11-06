# Άσκηση 2: μέσος όρος, μέγιστος και ελάχιστος βαθμός από το input2.txt

f = open("input2.txt")
grades = []
for line in f:
    parts = line.split()
    grades.append(float(parts[2]))
f.close()

print(f"Ο μέσος όρος των βαθμών είναι {sum(grades) / len(grades)}")
print(f"Ο μεγαλύτερος βαθμός είναι {max(grades)}")
print(f"Ο μικρότερος βαθμός είναι {min(grades)}")
