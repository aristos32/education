# M3_ask11.py · Λύση / Solution
# Επιπρόσθετη 3: ⭐⭐ Κατανάλωση καυσίμου αυτοκινήτου
# Παράδειγμα / Example: 500, 31, 1.5 → 6.2, 46.5

km = float(input('Χιλιόμετρα: '))
litra = float(input('Λίτρα καυσίμου: '))
timi = float(input('Τιμή λίτρου (€): '))
katanalosi = litra / km * 100
kostos = litra * timi
print('Κατανάλωση:', '%.1f' % katanalosi, 'λίτρα ανά 100 km')
print('Κόστος καυσίμου:', '%.2f' % kostos, '€')
