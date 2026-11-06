# Άσκηση 4: πόσες φορές υπάρχει ένας χαρακτήρας σε ένα string

def countCharInString(s, c):
    return s.count(c)


text = input("Give a string: ")
char = input("Give a char you want: ")
times = countCharInString(text, char)
print(f"The character {char} appears {times} times in the string {text}")
