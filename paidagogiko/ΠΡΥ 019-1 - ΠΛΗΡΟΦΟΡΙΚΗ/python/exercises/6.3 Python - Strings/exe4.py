# Άσκηση 4: συμπίεση συνεχόμενων χαρακτήρων, π.χ. AAAAAB -> 5AB

s = input("Give a string: ")

result = ""
i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j = j + 1
    count = j - i
    # ο ένας χαρακτήρας μένει ως έχει, χωρίς το 1 μπροστά
    if count > 1:
        result = result + str(count)
    result = result + s[i]
    i = j

print(f"Compressed string: {result}")
