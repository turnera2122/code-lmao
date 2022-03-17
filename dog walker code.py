price = 22.50
print("hello and welcome to dogsRus")
loop = True
dog_name = ""
while loop:
    print("1: Pick up dog\n2: Drop of dog\n3: List all staying dogs\nX: Exit program")
    option = input("what option would you like to choose? ")
    section = ["Betty", "Dog"]

    if option == "1":
        dog_name = input("enter dogs name: ")
        if dog_name in section:
            section.remove(dog_name)
            days = float(input("how many days has your dog been staying? "))
            print(f"the amount for 1 dog for {days} days is ${days * price:.2f}")
            print(f"{dog_name} has been removed from the roll")
        else:
            print("apologies a dog of that name has not been found")
    elif option == "2":
        dog_name = input("enter dogs name: ")
        section.insert(dog_name)
    elif option == "3":
        print(f"{section} is the name of all staying dogs")
    elif option.upper() == "X":
        loop = False
    else:
        print("Invalid option")
        print(f"Exiting")
