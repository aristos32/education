# Άσκηση 3: πόσοι διαιρέτες έχει ο Ν

n = int(input("Δώσε ένα θετικό ακέραιο αριθμό: "))

count = 0
for d in range(1, n + 1):
    if n % d == 0:
        count = count + 1

print(f"O αριθμός {n} έχει {count} διαιρέτες")
