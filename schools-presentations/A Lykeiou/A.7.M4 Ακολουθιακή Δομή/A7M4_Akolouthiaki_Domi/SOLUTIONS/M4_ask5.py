# M4_ask5.py · Λύση / Solution
# Επιπρόσθετη 1: ⭐ Σκιασμένο εμβαδόν: κύκλος μέσα σε τετράγωνο
# Παράδειγμα / Example: 10 → 21.5

X = float(input('Πλευρά τετραγώνου X: '))
R = X / 2
Etetr = X**2
Ekykl = 3.14 * R**2
Esk = Etetr - Ekykl
print('Σκιασμένο εμβαδόν:', '%.2f' % Esk)
