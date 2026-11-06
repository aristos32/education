# Άσκηση 2: ο μεγαλύτερος από τρεις αριθμούς

def max3(x, y, z):
    m = x
    if y > m:
        m = y
    if z > m:
        m = z
    return m


print(max3(4, 6, 2))
