# Άσκηση 2: 5^2 + 10^2 + 15^2 + ... μέχρι το S να ξεπεράσει το 5000

s = 0
multiple = 5
while s <= 5000:
    s = s + multiple ** 2
    last = multiple
    multiple = multiple + 5

print(f"Το άθροισμα S είναι ίσο με {s}")
print(f"Το τελευταίο πολλαπλάσιο του 5 υψωμένο στο τετράγωνο είναι {last}")
