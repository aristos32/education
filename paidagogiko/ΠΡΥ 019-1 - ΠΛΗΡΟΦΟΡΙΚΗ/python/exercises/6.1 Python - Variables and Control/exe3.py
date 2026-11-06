# Άσκηση 3: ο μεγαλύτερος από δύο πραγματικούς

x = float(input("Dose enan arithmo x: "))
y = float(input("Dose enan arithmo y: "))

if x >= y:
    biggest = x
else:
    biggest = y

# οι ακέραιες τιμές τυπώνονται χωρίς .0, όπως στο παράδειγμα
if biggest == int(biggest):
    biggest = int(biggest)

print(f"{biggest} is the biggest")
