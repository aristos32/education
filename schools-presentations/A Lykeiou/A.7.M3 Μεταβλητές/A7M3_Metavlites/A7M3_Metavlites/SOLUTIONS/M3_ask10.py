# M3_ask10.py · Λύση / Solution
# Επιπρόσθετη 2: ⭐⭐ Εισιτήρια κινηματογράφου και ρέστα
# Παράδειγμα / Example: 2, 3, 50 → 32.0, 18.0

enilikes = int(input('Εισιτήρια ενηλίκων: '))
paidia = int(input('Παιδικά εισιτήρια: '))
plironei = float(input('Πληρώνει (€): '))
synolo = enilikes * 8.5 + paidia * 5
resta = plironei - synolo
print('Σύνολο:', '%.2f' % synolo)
print('Ρέστα:', '%.2f' % resta)
