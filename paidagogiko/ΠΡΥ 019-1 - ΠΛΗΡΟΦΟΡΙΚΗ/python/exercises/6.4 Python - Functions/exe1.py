# Άσκηση 1: κλήση της myFunction(5)
# για x=5 το i παίρνει 0..4 και τα γινόμενα είναι 0+0+2+6+12 = 20

def myFunction(x):
    total = 0
    for i in range(x):
        total = total + i * (i - 1)
    return total


print(myFunction(5))
