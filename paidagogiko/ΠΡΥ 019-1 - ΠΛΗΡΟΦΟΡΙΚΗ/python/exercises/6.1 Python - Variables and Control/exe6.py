# Άσκηση 6: κόστος με ποιότητα, συσκευές, φοιτητή και ετήσια πληρωμή

price = int(input("Δώσε τιμή βασικού πακέτου: "))
quality = int(input("Δώσε ποιότητα (1=Basic, 2=Standard, 3=Premium): "))
devices = int(input("Δώσε αριθμό συσκευών (1-4): "))
is_student = int(input("Είσαι φοιτητής; (1=ΝΑΙ, 0=ΟΧΙ): "))
yearly = int(input("Ετήσια συνδρομή; (1=ΝΑΙ, 0=ΟΧΙ): "))

quality_cost = 0
if quality == 2:
    quality_cost = 7
elif quality == 3:
    quality_cost = 11

device_cost = 0
if devices == 2:
    device_cost = 3
elif devices == 3:
    device_cost = 6
elif devices == 4:
    device_cost = 9

student_discount = 1.0
if is_student == 1:
    student_discount = 0.75

yearly_discount = 1.0
if yearly == 1:
    yearly_discount = 0.9

cost = (price + quality_cost + device_cost) * student_discount * yearly_discount
print(f"Μηνιαίο Κόστος: ({price} + {quality_cost} + {device_cost}) * {student_discount} * {yearly_discount} = {cost} Ευρώ")
