import math

# read inputs
x = int(input("Δώσε ένα θετικό ακέραιο αριθμό (x):"))
n = int(input("Δώσε τον αριθμό των όρων (n) του αθροίσματος:"))

# calculate
factor = -1
result = 1
power = 2
for i in range(1,n):
    result = result + factor * x**power / math.factorial(power)
    factor = -1 * factor
    power = power + 2


# print result
print(f"Το άθροισμα της σειράς είναι {result}") 
