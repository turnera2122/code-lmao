password = "chicken"
attempt = "false"
guessedpassword = ""
while attempt != password:
    attempt = input("input password: ")
    if guessedpassword == password:
        print("access granted")
        print("Secret here")

    elif guessedpassword != password:
        print("entry denied")






