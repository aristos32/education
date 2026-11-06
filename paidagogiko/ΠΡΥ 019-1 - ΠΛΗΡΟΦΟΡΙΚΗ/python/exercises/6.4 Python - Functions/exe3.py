# Άσκηση 3: δίσεκτο αν διαιρείται με 4 αλλά όχι με 100, ή αν διαιρείται με 400

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


print(leap_year(1996))
print(leap_year(2100))
