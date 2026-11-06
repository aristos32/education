# Άσκηση 4: μέγιστος, θέση και μήκος σειράς. Τέλος με 0 ή αρνητικό.

print("Tha dineis thetikoys akeraious arithmous, ena-ena tin fora.")
print("Gia na stamatiseis dwse to 0 h arnitiko arithmo.")

count = 0
maximum = 0
position = 0
n = int(input("Dwse arithmo 1: "))

while n > 0:
    count = count + 1
    if n > maximum:
        maximum = n
        position = count
    n = int(input(f"Dwse arithmo {count + 1}: "))

print(f"O megistos einai o {maximum} kai einai o {position}os arithmos mias seiras megethous {count}")
