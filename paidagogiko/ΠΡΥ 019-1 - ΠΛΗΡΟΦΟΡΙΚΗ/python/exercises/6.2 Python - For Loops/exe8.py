# Άσκηση 8: 1 - x^2/2! + x^4/4! - x^6/6! + ... για n όρους

x = int(input("Δώσε ένα θετικό ακέραιο αριθμό (x): "))
n = int(input("Δώσε τον αριθμό των όρων (n) του αθροίσματος: "))

result = 1
sign = -1
power = 2
for i in range(1, n):
    fact = 1
    for k in range(1, power + 1):
        fact = fact * k
    result = result + sign * x ** power / fact
    sign = -sign
    power = power + 2

print(f"Το άθροισμα της σειράς είναι {result}")
