# Άσκηση 5: ζυγοί ανάμεσα σε Α και Β, μαζί με τα άκρα

def printEvenBetween(a, b):
    if a > b:
        a, b = b, a
    for n in range(a, b + 1):
        if n % 2 == 0:
            print(n, end=" ")
    print()


a = int(input("Give first number: "))
b = int(input("Give second number: "))
printEvenBetween(a, b)
