import random
number = random.randint(1, 20)

guess = int(input("guess the number: "))
while guess != number:
    if guess < number:
        guess = int(input("too low try again:"))
    else:
        guess = int(input("too high try again: "))
        print("mario")
