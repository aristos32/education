# Άσκηση 6: συνάρτηση reverse12 και κλήση από το κυρίως πρόγραμμα

def reverse12(n):
    multiples = []
    for i in range(1, 13):
        multiples.append(n * i)
    multiples.reverse()
    return multiples


n = int(input("Δώσε ένα αριθμό: "))
print(reverse12(n))
