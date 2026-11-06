# Άσκηση 7: ακέραιος από 1 έως 10000 με τους περισσότερους διαιρέτες

best = 1
most = 1

for n in range(1, 10001):
    # κάθε διαιρέτης d δίνει και τον n // d
    count = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            count = count + 1
            if d * d != n:
                count = count + 1
        d = d + 1
    if count > most:
        most = count
        best = n

print(f"The maximum number of divisors is {most}")
print(f"A number with {most} divisors is {best}")
