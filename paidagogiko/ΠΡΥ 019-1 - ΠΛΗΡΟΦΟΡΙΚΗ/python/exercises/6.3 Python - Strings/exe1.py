# Άσκηση 1: πρώτος/τελευταίος χαρακτήρας, πρώτο κενό, πρώτη λέξη

s = input("Δώσε μια συμβολοσειρά: ")

print(s[0])
print(s[-1])
print(s[len(s) - 1])

space = s.index(" ")
print(space)
print(s[0:space])
