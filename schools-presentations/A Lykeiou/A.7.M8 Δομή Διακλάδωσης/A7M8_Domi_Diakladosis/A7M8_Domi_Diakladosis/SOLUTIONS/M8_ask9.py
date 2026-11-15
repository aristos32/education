# M8_ask9.py · Λύση / Solution
# Επιπρόσθετη 6: ⭐⭐⭐ Κλιμακωτός λογαριασμός νερού
# Παράδειγμα / Example: 8 → 4.0

m3 = float(input('Κυβικά μέτρα: '))
if m3 <= 10:
    kostos = m3 * 0.5
else:
    kostos = 10 * 0.5 + (m3 - 10) * 1.2
print('Λογαριασμός:', '%.2f' % kostos)
