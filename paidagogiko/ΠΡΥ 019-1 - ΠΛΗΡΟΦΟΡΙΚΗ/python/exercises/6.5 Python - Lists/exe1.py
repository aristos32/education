# Άσκηση 1: λίστα με τις μέρες της εβδομάδας

days = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]

print("Ερώτημα (α)")
print(days)

print("Ερώτημα (β)")
for day in days:
    print(day)

print("Ερώτημα (γ)")
for i in range(len(days)):
    print(days[i], i + 1)
