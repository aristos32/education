# Άσκηση 7: 2 + 22 + 222 + ... μέχρι n όρους

n = int(input("Δώσε ένα θετικό ακέραιο αριθμό: "))

term = 0
total = 0
text = ""
for i in range(n):
    term = term * 10 + 2
    total = total + term
    if i > 0:
        text = text + "+"
    text = text + str(term)

print(f"{text} = {total}")
