# M5_ask6.py · Λύση / Solution
# Επιπρόσθετη 3: ⭐⭐ Έκπτωση και ΦΠΑ
# Παράδειγμα / Example: 100, 20 → 95.2

timi = float(input('Αρχική τιμή (€): '))
ekptosi = float(input('Έκπτωση (%): '))
meta = timi * (1 - ekptosi/100)
telikh = meta * 1.19
print('Τελική τιμή:', '%.2f' % telikh)
