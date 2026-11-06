# Άσκηση 4: μάντεμα κωδικού, το πολύ 5 προσπάθειες

code = "myPass"
found = False

for attempt in range(5):
    guess = input("Γράψε ένα κωδικό: ")
    if guess == code:
        print("Συγχαρητήρια, βρήκες τον κωδικό.")
        found = True
        break
    # στην 5η αποτυχία τυπώνεται μόνο το μήνυμα αποτυχίας
    if attempt < 4:
        print("Λανθασμένη προσπάθεια, ξαναδοκίμασε.")

if not found:
    print("Απέτυχες να βρεις τον κωδικό.")
