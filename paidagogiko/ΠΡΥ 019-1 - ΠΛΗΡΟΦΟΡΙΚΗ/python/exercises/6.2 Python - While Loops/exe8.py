# Άσκηση 8: πίνακας προπαίδειας 1-10

print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

for row in range(1, 11):
    print(f"{row:4}", end="")
    for col in range(1, 11):
        print(f"{row * col:4}", end="")
    print()
