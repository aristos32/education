# M3_ask12.py · Λύση / Solution
# Επιπρόσθετη 4: ⭐⭐⭐ Μοιράζοντας πίτσες (κρυμμένα λάθη)
# Παράδειγμα / Example: 3, 5 → 4, 4

pizzes = int(input('Πίτσες: '))
kommatia = 8
synolo = pizzes * kommatia
atoma = int(input('Άτομα: '))
kathe_enas = synolo // atoma
perisseuoun = synolo % atoma
print('Κομμάτια για τον καθένα:', kathe_enas)
print('Περισσεύουν:', perisseuoun)
