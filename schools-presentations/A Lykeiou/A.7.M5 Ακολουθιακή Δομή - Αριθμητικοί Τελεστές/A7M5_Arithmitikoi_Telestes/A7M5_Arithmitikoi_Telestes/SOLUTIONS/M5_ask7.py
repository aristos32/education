# M5_ask7.py · Λύση / Solution
# Επιπρόσθετη 4: ⭐⭐⭐ Εμβαδόν τριγώνου: ο τύπος του Ήρωνα
# Παράδειγμα / Example: 3, 4, 5 → 6

a = float(input('Πλευρά a: '))
b = float(input('Πλευρά b: '))
c = float(input('Πλευρά c: '))
s = (a + b + c) / 2
E = (s * (s - a) * (s - b) * (s - c))**0.5
print('Εμβαδόν:', '%.2f' % E)
