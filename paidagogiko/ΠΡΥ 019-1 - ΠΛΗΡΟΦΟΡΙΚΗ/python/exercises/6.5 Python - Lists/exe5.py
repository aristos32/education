# Άσκηση 5: τα 12 πρώτα πολλαπλάσια, αντίστροφα

n = int(input("Δώσε ένα αριθμό: "))

pollaplasia = []
for i in range(1, 13):
    pollaplasia.append(n * i)
pollaplasia.reverse()

print(pollaplasia)
