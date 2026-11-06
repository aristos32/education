# Άσκηση 5: μάντεμα τυχαίου αριθμού 1-9, έξοδος με exit

import random

number = random.randint(1, 9)
attempts = 0
prompt = "Please enter a number from 1 to 9, or type 'exit' to exit the game: "

guess = input(prompt)
while guess != "exit":
    attempts = attempts + 1
    value = int(guess)
    if value == number:
        print("You got it!")
        break
    if value > number:
        print("Too high!")
    else:
        print("Too low!")
    guess = input(prompt)

print(f"And it only took you {attempts} attempts")
