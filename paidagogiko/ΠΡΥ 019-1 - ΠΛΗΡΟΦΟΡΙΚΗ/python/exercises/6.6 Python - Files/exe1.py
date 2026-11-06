# Άσκηση 1: γράψε 1..20 στο file1.txt και μετά άθροισέ τα

f = open("file1.txt", "w")
for n in range(1, 21):
    f.write(str(n) + "\n")
f.close()

f = open("file1.txt")
total = 0
for line in f:
    total = total + int(line)
f.close()

print(f"Το άθροισμα είναι {total}")
