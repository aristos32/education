# variable declarations
price = int(input("Δώσε τιμή βασικού πακέτου: "))
quality = int(input("Δώσε ποιότητα (1=Basic, 2=Standard, 3=Premium): "))
devices = int(input("Δώσε αριθμό συσκευών (1-4): "))
is_student = int(input("Είσαι φοιτητής; (1=ΝΑΙ, 0=ΟΧΙ): "))
yearly = int(input("Ετήσια συνδρομή; (1=ΝΑΙ, 0=ΟΧΙ): "))
quality_cost = 0
device_cost = 0
student_discount_percentage = 1
addtional_discount_percentage = 1
monthly_cost = 0

# intermediary calculations
if quality == 2:
    quality_cost = 7
elif quality == 3:
    quality_cost = 11

if devices == 2:
    device_cost = 3
elif devices == 3:
    device_cost = 6
elif devices == 4:
    device_cost = 9

if is_student == 1:
    student_discount_percentage = 0.75

if yearly == 1:
    addtional_discount_percentage = 0.9

# final calculation
monthly_cost = ( price + quality_cost + device_cost ) * student_discount_percentage * addtional_discount_percentage

# print result
print(f"Μηνιαίο Κόστος: ( {price} + {quality_cost} + {device_cost} ) * {student_discount_percentage} * {addtional_discount_percentage} = {monthly_cost} Ευρώ")
