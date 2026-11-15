# M8_ask8.py · Λύση / Solution
# Επιπρόσθετη 5: ⭐⭐ Ταξί με έκπτωση
# Παράδειγμα / Example: 10 → 13.0

km = float(input('Χιλιόμετρα: '))
kostos = 4 + 0.9 * km
if km > 20:
    kostos = kostos * 0.9
print('Πληρωμή:', '%.2f' % kostos)
