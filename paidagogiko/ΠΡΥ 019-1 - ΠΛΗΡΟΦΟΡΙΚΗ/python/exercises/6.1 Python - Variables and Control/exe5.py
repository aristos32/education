# Άσκηση 5: κόστος = (τιμή + χρέωση ποιότητας) * έκπτωση φοιτητή

price = int(input("Δώσε τιμή βασικού πακέτου: "))
quality = int(input("Δώσε ποιότητα (1=Basic, 2=Standard, 3=Premium): "))
is_student = int(input("Είσαι φοιτητής; (1=ΝΑΙ, 0=ΟΧΙ): "))

extra_cost = 0
if quality == 2:
    extra_cost = 7
elif quality == 3:
    extra_cost = 11

discount = 1.0
if is_student == 1:
    discount = 0.75

cost = (price + extra_cost) * discount
print(f"Μηνιαίο Κόστος: ({price} + {extra_cost}) * {discount} = {cost} Ευρώ")
