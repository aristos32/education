# Άσκηση 5: αριθμοί ανάμεσα σε δύο όρια που διαιρούνται με το 3

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

# η range θέλει το μικρό όριο πρώτο
start = a
end = b
if start > end:
    temp = start
    start = end
    end = temp

print(f"Numbers between {a} and {b} that are divisible by 3:", end=" ")
for n in range(start, end + 1):
    if n % 3 == 0:
        print(n, end=" ")
print()
