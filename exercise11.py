import random
number: object = random.randint(1, 100)
count = 0
mode = ""
# print(number)
while mode!= "E" and mode != "H":
    mode = input("which mode do you want: E for easy or H for hard: ")
    if mode == "E":
        max_guesses = 10
    else:
        max_guesses = 21
        guess = int(input("guess the number: "))
while guess != number and count <max_guesses:
 count += 1
if guess < number:
        guess= int(input("too low try again: "))
else:
        guess = int(input("too high, try again: "))
if guess == number:
        print(f"you got it in {count} gueses!")
else:
        print("you coudnt get it in 10 guesses!")

