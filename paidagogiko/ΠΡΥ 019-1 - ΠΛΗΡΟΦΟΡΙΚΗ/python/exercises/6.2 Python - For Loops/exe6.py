# Άσκηση 6: σύνολο, μέσος όρος, μέρες πάνω από 3 ώρες, μέγιστο

total = 0
days_over = 0
max_hours = 0
max_day = 1

for day in range(1, 8):
    hours = int(input(f"{day}η μέρα της εβδομάδας: "))
    total = total + hours
    if hours > 3:
        days_over = days_over + 1
    if hours > max_hours:
        max_hours = hours
        max_day = day

print(f"Συνολικές ώρες: {total}")
print(f"Μέσος όρος ωρών ανά μέρα: {total / 7}")
print(f"Αριθμός ημερών πάνω από 3 ώρες: {days_over}")
print(f"Μέγιστος αριθμός ωρών σε μια μέρα: {max_hours} ({max_day}η μέρα)")
