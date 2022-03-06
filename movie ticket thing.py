def ticket_payout():

    print("welcome to boku boku cinemas")
    pass
ticket_payout()
loop = 0
child = 12
student = 14
adult = 18
total = ()
while loop == 0:
    print("Which tickets do you want?")
    print("1, child $12")
    print("2, student $14")
    print("3, adult $18")
    ticket = int(input("choose your ticket: "))
    if ticket == 1:
        price = 12
    elif ticket == 2:
        price = 14
    elif ticket == 3:
        price = 18
    else:
        price = 0
        print("please enter a valid answer")
    amount = int(input("how many of that ticket?"))
    temptotal = amount * price
    total = + temptotal
    print(f"your current total is {total}")
    again = input("Do you want to buy more tickets? (y/n)")
    if again == "n":
        loop = 1
    else:
        print("Restarting")
exit(f"Your final total is {total}")
