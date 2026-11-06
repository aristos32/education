# header row
print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

# multiplication table
for row in range(1, 11):
    print(f"{row:4}", end="")
    for col in range(1, 11):
        print(f"{row * col:4}", end="")
    print()
    print()
