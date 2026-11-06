# Άσκηση 3: έγκυρος κωδικός = τουλάχιστον 2 ψηφία και 1 κεφαλαίο

code = input("Δώσε κωδικό τιμολογίου: ")

digits = 0
upper = 0
lower = 0
for c in code:
    if c.isdigit():
        digits = digits + 1
    if c.isupper():
        upper = upper + 1
    if c.islower():
        lower = lower + 1

print(f"Πλήθος ψηφίων: {digits}")
print(f"Πλήθος κεφαλαίων γραμμάτων: {upper}")
print(f"Πλήθος μικρών γραμμάτων: {lower}")

if digits >= 2 and upper >= 1:
    print("Το τιμολόγιο είναι: Έγκυρο")
else:
    print("Το τιμολόγιο είναι: Άκυρο")
