number = 0
while number <=100:
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz)")
    elif number % 3 == 0:
        print("fuzz)")
    elif number % 5 == 0:
        print("buzz")
    else:
        print (number)
        number+=1
    print("all done")
