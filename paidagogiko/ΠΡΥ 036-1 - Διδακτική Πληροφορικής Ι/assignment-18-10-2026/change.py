# Enter your code here. Read input from STDIN. Print output to STDOUT
money = float(input())
cost = float(input())
remainder = money - cost

#f = fixed-point decimal notation (float)
#.2 = show 2 digits after the decimal point
#print(f"{remainder:.2f}")

#remove trailing zeros
print(f"{remainder:g}")